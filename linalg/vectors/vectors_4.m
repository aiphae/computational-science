v1 = [1 2 3 4 5 6];
v2 = [0 -4 -3 6 5 1];

% method 1
% .* is an element wise multiplication
dot_product = sum(v1 .* v2);

% method 2
dot_product = dot(v1, v2);

% method 3
dot_product = v1 * v2';

% method 4
dp = 0;
for i = 1: length(v1)
    dp = dp + v1(i) + v2(i);
end
