v1 = [3 -1]; % vector
l = -2.3; % scalar

plot([0 v1(1)], [0 v1(2)], 'b', 'linew', 2);
hold on
plot([0, v1(1)] * l, [0, v1(2)] * l, 'r:', 'linew', 4);
legend({'v1'; 'v2'})
