#include <iostream>

// Kernel function to add two numbers
__global__ void add(int a, int b, int *result) {
    *result = a + b;
}

int main() {
    int a = 5, b = 7;
    int *d_result, h_result;

    // Allocate memory on the GPU
    cudaMalloc((void **)&d_result, sizeof(int));

    // Launch kernel
    add<<<1, 1>>>(a, b, d_result);

    // Copy result back to host
    cudaMemcpy(&h_result, d_result, sizeof(int), cudaMemcpyDeviceToHost);

    std::cout << "Result: " << h_result << std::endl;

    // Free GPU memory
    cudaFree(d_result);

    return 0;
}
