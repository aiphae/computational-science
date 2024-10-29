#include <Eigen/Dense>
#include <iostream>

int main() {
    int m = 4, n = 6;

    Eigen::MatrixXd A = Eigen::MatrixXd::Random(m, n);
    Eigen::MatrixXd B = Eigen::MatrixXd::Random(m, n);

    std::cout << "A:\n" << A << "\n\n";
    std::cout << "B:\n" << B << "\n\n";

    // Method 1
    Eigen::VectorXd dPs(n);
    for (int i = 0; i < n; ++i) {
        double sum = 0;
        for (int j = 0; j < m; ++j) {
            sum += A(j, i) * B(j, i);
        }
        dPs[i] = sum;
    }
    std::cout << "Dot products:\n" << dPs << "\n\n";
}
