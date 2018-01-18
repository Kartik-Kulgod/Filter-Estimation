clear;clc;
tps = (1:1:15);%Not included zero for ease of calculation
x = randn(1,300);% A white random process of variance 1
h = sin(tps)./(tps);
y = filter(h,1,x);
N = length(h);
%Tx = length(x);
for i = 1:N
    rx(i) = ([x,zeros(1,i-1)]*[zeros(i-1,1);x'])/N;
    ryx(i) = ([y,zeros(1,i-1)]*[zeros(i-1,1);x'])/N;
end
hest = inv(toeplitz(rx))*ryx';
plot((0:N-1),hest,'o',(0:N-1),h,'x')
