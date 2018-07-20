function sum_res_squared = olivineMCbestfitplot(x0)
global H2O
global H2O_meas
global radius
global P0
global Pf
global dist
global Solex_P_H2O


DH2O = 1e12*10^(x0(1));  % diffusivity in um2/s
dPbydt = x0(3);   % decompression rate in bars/s from Ferguson
t_tot = (P0-Pf)/dPbydt;



numx = 101;   %number of grid points in x
numt = 200000;  %number of time steps to be iterated
dx = radius/(numx - 1);
dt = t_tot/(numt - 1);
t = 0:dt:t_tot;
%dt = 0.01*radius*(dx^2)/DH2O;
%numt = (t_tot/dt)+1;
dP = -dt*dPbydt;
Pvec = P0:dP:Pf;
load Solex_P_H2O.txt
H2O_melt_vec = spline(Solex_P_H2O(:,1),Solex_P_H2O(:,2),Pvec);
H2O_ol_BC = H2O_melt_vec*x0(2);     % calculates conc at edge of olivine at each timestep based on measured partition coefficient.


figure(1)
subplot(1, 3, 1)
plot(Pvec, H2O_melt_vec, '-b', 'linewidth', 2)
axis square
xlabel('Pressure (bars)')
ylabel('H_2O in melt (wt%)')
set(gca, 'FontSize', 12)
subplot(1, 3, 2)
plot(t, Pvec, '-b', 'linewidth', 2)
axis square
xlabel('Time (s)')
ylabel('Pressure (bars)')
set(gca, 'FontSize', 12)
subplot(1, 3, 3)
plot(t, H2O_ol_BC, '-b', 'linewidth', 2)
axis square
xlabel('Time (s)')
ylabel('Water at edge of olivine (ppm)')
set(gca, 'FontSize', 12)

x = 0:dx:radius;   %vector of x values, to be used for plotting

C = zeros(numx,numt);   %initialize everything to zero

%specify initial conditions
C(:,1) = H2O_ol_BC(1);


%iterate difference equations
for j=1:numt-1
   t(j+1) = t(j) + dt;

   for i=2:numx-1
      C(i,j+1) = C(i,j) + (DH2O*dt/(dx^2))*(C(i+1,j) - 2*C(i,j) + C(i-1,j)); 
   end
   C(numx,j+1) = H2O_ol_BC(j+1);          % degassing boundary condition
   C(1,j+1) = C(2,j+1);  %C(1,j+1) found from no-flux condition
end

%absdist = abs(dist);
%H2Omodel = spline(x,C(:,numt),absdist);
%figure(10)
%plot(absdist, H2Omodel, 'o')
%residuals = H2O - H2Omodel;
%res_squared = residuals.^2;
%sum_res_squared = sum(res_squared)/length(H2Omodel);


x_mm = x/1000;

figure(2);
hold on;
y=H2O_meas;
margin = 0.6;
ciplot(y-margin, y+margin, dist/1000, [0.9 0.9 0.9])
ph1=plot(x_mm,C(:,1), '--k', 'linewidth', 2, 'displayname', 'Initial condition');
plot(-x_mm,C(:,1), '--k', 'linewidth', 2);
ph2=plot(x_mm,C(:,numt), '-k', 'linewidth', 2, 'displayname', 'Best-fit model');
plot(-x_mm, C(:,numt),'-k', 'linewidth', 2);
ph5=plot(dist/1000, y, 'ob', 'markersize', 10, 'linewidth', 2, 'displayname', 'Measured water concentration (ppm)');
xlabel('Distance along [100] (mm)');
ylabel('Bulk hydrogen (ppm H_2O)');
set(gca,'fontsize', 20)

set(gcf, 'PaperUnits', 'inches');
orient portrait
papersize = get(gcf, 'PaperSize');
width =6;         % Initialize a variable for width.
height = 6;          % Initialize a variable for height.
left = (papersize(1)- width)/2;
bottom = (papersize(2)- height)/2;
myfiguresize = [left, bottom, width, height];
set(gcf, 'PaperPosition', myfiguresize);

print -dsvg -r600 KIki_fig11_Jun4
print -dpdf -r600 KIki_fig11_Jun4

end