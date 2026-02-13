# Python and High-Performance Computing

Pythong and HPC at the Technical University of Denmark. This course goes through how to write efficient Python code and leverage parallel computing to solve computationally intensive problems. 

**Topics:** NumPy, Parallel Processing, Performance Optimization, Large Data Handling, HPC Job Scheduling, High-Performance Computing Course

---

## Weekly Breakdown

### **Week 1: Introduction & Basics**
- Setup and Python fundamentals
- File I/O operations
- Batch job scripting fundamentals (BSUB)

### **Week 2: NumPy Fundamentals**
- Vector and matrix operations
- NumPy array operations and manipulation
- Linear algebra operations
- Performance comparison with pure Python

### **Week 3: NumPy Advanced Operations**
- Array indexing and slicing
- Broadcasting fundamentals
- Vectorization techniques
- Performance benchmarking

### **Week 4: Broadcasting & Geospatial Computing**
- Advanced broadcasting patterns
- Haversine distance calculations (geographical applications)
- Vectorized mathematical operations

### **Week 5-6: Parallel Processing**
- Multiprocessing and process pools
- Parallel algorithm design
- Reduction operations (full vs. parallel)
- Mandelbrot set computation (CPU parallelization case study)

### **Week 7: Optimization Techniques I**
- Code profiling and optimization
- Algorithm refinement
- Memory-efficient implementations

### **Week 8: Large Data Handling**
- Memory-mapped arrays (NumPy memmap)
- Zarr arrays for chunked storage
- Data downscaling techniques
- Pandas chunked operations
- Out-of-core computing strategies

### **Week 9: Advanced Processing**
- Specialized algorithms and techniques
- Performance optimization case studies

### **Week 10: Optimization Challenges**
- Complex performance problems
- Algorithm optimization strategies

### **Week 11: Batch Job Scheduling**
- Advanced BSUB job array syntax
- Parallel job execution patterns
- Wait and synchronization mechanisms

### **Week 13: Matrix Multiplication & Final Topics**
- Optimized matrix multiplication
- Performance analysis

---

## Key Topics Covered

- **NumPy**: arrays, linear algebra, broadcasting, vectorization
- **Parallel Computing**: multiprocessing, process pools, distributed algorithms
- **Performance Optimization**: profiling, memory management, algorithm design
- **Large Data**: memory mapping, chunked processing, Zarr format
- **HPC Job Scheduling**: BSUB job arrays, batch processing, resource management
- **Case Studies**: Mandelbrot set, matrix operations, geographical computing

---

## Project Structure

```
Week_1/          - Introduction and job scripting basics
Week_2/          - NumPy fundamentals and linear algebra
Week_3/          - NumPy advanced operations and benchmarking
Week_4/          - Broadcasting and geospatial computing
Week_5_6/        - Parallel processing and multiprocessing
Week_7/          - Optimization techniques
Week_8/          - Large data handling (memmap, zarr, downscaling)
Week_9/          - Advanced processing algorithms
Week_10/         - Performance optimization challenges
Week_11/         - Batch job scheduling and arrays
Week_13/         - Matrix multiplication and capstone topics
```

---

## Notes

- Many scripts are designed for DTU HPC environment (requires BSUB scheduler)
- Some exercises reference external datasets and autolab submissions
- Performance scripts expect specific hardware configurations
- NumPy binary files (.npy) and Zarr arrays included for data persistence
