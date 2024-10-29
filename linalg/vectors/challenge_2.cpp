#include <Eigen/Dense>
#include <iostream>

int main() {
    Eigen::RowVectorXd A = Eigen::RowVectorXd::Random(100);
    Eigen::RowVectorXd B = Eigen::RowVectorXd::Random(100);

    std::cout << "A dot B: " << A.dot(B) << "\n";
    std::cout << "B dot A: " << B.dot(A) << "\n";

    Eigen::RowVectorXd C(2);
    C << 1, 2;
    Eigen::RowVectorXd D(2);
    D << 3, 4;

    std::cout << "C dot D: " << C.dot(D) << "\n";
    std::cout << "D dot C: " << D.dot(C) << "\n"; 
}
