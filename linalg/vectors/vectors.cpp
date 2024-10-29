#include <Eigen/Dense>
#include <iostream>

int main() {
    Eigen::VectorXd v1(6), v2(6), v3(6), v4(6);
    v1 << 1, 2, 3, 4, 5, 6;
    v2 << -1, -2, -3, -4, -11, -6;

    v3 = v1 + v2;
    v4 = -1.2 * v3;

    int dot = v3.dot(v4);
    std::cout << dot << std::endl;

    int sum = 0;
    for (int i = 0; i < v3.size(); ++i) {
        sum += v3[i] * v4[i];
    }
    std::cout << sum << std::endl;
}
