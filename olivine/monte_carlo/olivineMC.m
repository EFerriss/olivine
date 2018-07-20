function sum_res_squared = olivineMC(x0)
%x0=[-9 14  
global H2O
global H2O_meas
global radius
global P0
global Pf
global dist
global Solex_P_H2O


DH2O = 1e12*10^(x0(1));  % diffusivity in um2/s
dPbydt = x0(3);   % decompression rate in bars/s from Ferguson et al. 2016
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
H2O_melt_vec = spline(Solex_P_H2O(:,1),Solex_P_H2O(:,2),Pvec);
H2O_ol_BC = H2O_melt_vec*x0(2);     % calculates conc at edge of olivine at each timestep based on measured partition coefficient.

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

absdist = abs(dist);

H2Omodel = spline(x,C(:,numt),absdist);
residuals = H2O - H2Omodel;
res_squared = residuals.^2;
sum_res_squared = sum(res_squared)/length(H2Omodel);

end
