A = randn(4, 6);
B = randn(4, 6);

dps = zeros(size(A, 2), 1);
for i = 1: size(A, 2)
    dps(i) = dot(A(:, i), B(:, i));
    disp(dps(i));
end
