% Script for calculating best-fit values of water diffusivity (DH2O), water
% partition coefficient (Kd) and magma decompression rate (dPbydt) from
% measured water concentration gradients across the 'a' axis of olivine
% phenocrysts. This example is set up for an olivine phenocryst from the
% Kilauea Iki 1959 fire-fountain eruption. Please see Ferriss et al. (2018)
% for further details, and contact Megan (newcombe@ldeo.columbia.edu) with
% questions.

% Required inputs are a text file containing water concentration in olivine data (column 1 is radial distance (um) and column 2 is water
% concentration (ppm)), and a text file containing pressure (bars) vs.
% water concentration in host magma (wt%). 


close all
clear all
global H2O_meas
global H2O
global radius
global P0
global Pf
global dist
global Solex_P_H2O

% Input files
load KilaueaIki2_dist_H2O.txt % column 1 is radial distance along 'a' in microns; column 2 is measured H2O in ppm
load Solex_P_H2O.txt % column 1 is pressure in bars; column 2 is concentration of water dissolved in melt (calculated by Solex or VolatileCalc)

radius = 640.5;     % radius of xal in microns
H2O_meas = KilaueaIki2_dist_H2O(:,2); % measured water concentration in olivine (ppm)
dist = KilaueaIki2_dist_H2O(:,1); % radial distance in microns
P0 = 1100;  % initial pressure in bars from Ferguson et al. 2016
Pf = 1;     % final pressure in bars from Ferguson et al. 2016

% Monte Carlo error analysis: Add random noise to the original H2O data to
% create p=# iterations synthetic H2O profiles. Fit each of these profiles.
% Choose starting values for  by testing n=500
% randomly selected starting values. 
% Reduce values of # iterations and p if program takes too long to run.
n=100;
p=100;

%Initialize variables
bestfit_parameters = zeros(p,3);
bestfit_DH2O = zeros(p, 1);
bestfit_Kd = zeros(p, 1);
bestfit_dPbydt = zeros(p, 1);
noisy_H2O_profiles = zeros(p, length(H2O));

results_ordered = zeros(n,4);
sar = zeros(1,n);

for k = 1:p
k

% add normally distributed noise to the data points to create synthetic
% water concentration gradients

one_sig = 0.3; % stdev of normal distribution based on central 5 data points of measured profile   
H2Onoise = addnoise(H2O_meas, one_sig);
H2O = H2Onoise;    

% Generate random starting positions for Monte Carlo analysis
x0(:,1) = rand(n,1)*2 - 11;  % log DH2O starting guess: mean of -10, stdev of 1
x0(:,2) = (rand(n,1)*3 + 8)/0.75;  % Partition coefficient (Kd) guess x10^4
x0(:,3) = rand(n,1)*0.05 + 0.45; % dP/dt in bar/s

% Calculate misfit of model at each starting position
for i = 1:n
    i
    sar(i) = olivineMC(x0(i,:));   %store values of sum of residuals, DH2O, Kd, and dPbydt.
end

% Sort results from lowest to highest misfit
results = [sar' x0];
[Y,I]=sort(results(:,1));
results_ordered=results(I,:);  %use the column indices from sort() to sort all columns of A.

clear x0
clear results

% Select the best result with the lowest misfit
x0 = results_ordered(1,2:4);
x0orig = x0;

% Now use fminsearch to find the best-fit values of D_H2O, Kd, dP/dt:

for j = 1
    j
    options = optimset('TolFun',0.1, 'TolX', 0.1);
    [x, fval, exitflag] = fminsearch(@olivineMC, x0, options);
    x0 = x;
  
end

bestfit_parameters(k, 1:3) = x0;
bestfit_DH2O(k, 1) = x0(1);
bestfit_Kd(k,1) = x0(2);
bestfit_dPbydt(k,1) = x0(3);
noisy_H2O_profiles(k, 1:length(H2O)) = H2O';
  
  clear x
  clear fval
  clear x0
   
end

overall_bestfit = [mean(bestfit_DH2O(:,1)) mean(bestfit_Kd(:,1)) mean(bestfit_dPbydt(:,1))];
olivineMCbestfitplot(overall_bestfit)

dlmwrite('bestfit_parameters.txt', bestfit_parameters)
dlmwrite('bestfit_DH2O.txt', bestfit_DH2O)
dlmwrite('bestfit_Kd.txt', bestfit_Kd)
dlmwrite('bestfit_dPbydt.txt', bestfit_dPbydt)
dlmwrite('noisy_H2O_profiles.txt', noisy_H2O_profiles)
dlmwrite('overall_bestfit.txt', overall_bestfit)

  clear x
  clear fval
  clear x0
  





