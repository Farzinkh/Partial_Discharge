
clc, clear, close all


data = importfile('prediction_per_actual.csv');

N = length(data); M = N/2;

% show R2 curves

% X
x_act = data(2:2:end, 1);
x_est = data(1:2:end, 1);
figure; plot(x_act - 500, x_est - 500, 'ok', 'LineWidth', 2, 'MarkerSize', 5); 
hold on; plot([-600, 600], [-600, 600], 'r', 'LineWidth', 2)
xlabel('x-actual (mm)', 'FontSize', 24); ylabel('x-estimated (mm)', 'FontSize', 24); 
set(gca, ...
    'Box'         , 'on'     , ...
    'FontSize'    ,24); 
grid on; axis xy; axis equal

% Y
x_act = data(2:2:end, 2);
x_est = data(1:2:end, 2);
figure; plot(x_act - 250, x_est - 250, 'ok', 'LineWidth', 2, 'MarkerSize', 5); 
hold on; plot([-300, 300], [-300, 300], 'r', 'LineWidth', 2)
xlabel('y-actual (mm)', 'FontSize', 24); ylabel('y-estimated (mm)', 'FontSize', 24); 
set(gca, ...
    'Box'         , 'on'     , ...
    'FontSize'    ,24); 
grid on; axis xy; axis equal

% z
x_act = data(2:2:end, 3);
x_est = data(1:2:end, 3);
figure; plot(x_act - 250, x_est - 250, 'ok', 'LineWidth', 2, 'MarkerSize', 5); 
hold on; plot([-300, 300], [-300, 300], 'r', 'LineWidth', 2)
xlabel('z-actual (mm)', 'FontSize', 24); ylabel('z-estimated (mm)', 'FontSize', 24); 
set(gca, ...
    'Box'         , 'on'     , ...
    'FontSize'    ,24); 
grid on; axis xy; axis equal
