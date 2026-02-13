# Python and High-Performance Computing Course

A comprehensive coursework covering Python optimization, parallel processing, NumPy, and high-performance computing techniques.

## Course Overview

This course explores practical techniques for writing efficient Python code and leveraging parallel computing to solve computationally intensive problems. It combines theory with hands-on exercises, progressively building from basic concepts to advanced optimization strategies.

**Duration:** 13 Weeks  
**Topics:** NumPy, Parallel Processing, Performance Optimization, Large Data Handling, HPC Job Scheduling

---

## Weekly Breakdown

### **Week 1: Introduction & Basics**
- Setup and Python fundamentals
- File I/O operations
- Batch job scripting fundamentals (BSUB)
- **Files:** hello_world.py, Job_Scripts_1-6.sh

### **Week 2: NumPy Fundamentals**
- Vector and matrix operations
- NumPy array operations and manipulation
- Linear algebra operations
- Performance comparison with pure Python
- **Files:** autolab_numpy_1-6.py/.sh, functions.py, matrix operations

### **Week 3: NumPy Advanced Operations**
- Array indexing and slicing
- Broadcasting fundamentals
- Vectorization techniques
- Performance benchmarking
- **Files:** exercise_1*.py, performance benchmarks, shell scripts

### **Week 4: Broadcasting & Geospatial Computing**
- Advanced broadcasting patterns
- Haversine distance calculations (geographical applications)
- Vectorized mathematical operations
- **Files:** broadcasting.py, Haversine.py

### **Week 5-6: Parallel Processing**
- Multiprocessing and process pools
- Parallel algorithm design
- Reduction operations (full vs. parallel)
- Mandelbrot set computation (CPU parallelization case study)
- **Files:** mandelbrot.py, mandelbrot_new.py, full_reduction.py, parallel_reduction.py, mandelbrot.sh

### **Week 7: Optimization Techniques I**
- Code profiling and optimization
- Algorithm refinement
- Memory-efficient implementations
- **Files:** 1.py - 5.py

### **Week 8: Large Data Handling**
- Memory-mapped arrays (NumPy memmap)
- Zarr arrays for chunked storage
- Data downscaling techniques
- Pandas chunked operations
- Out-of-core computing strategies
- **Files:** mandelbrot_memmap.py, mandelbrot_zarr.py, mandelbrot_downscale.py, Pandas_chunk.py

### **Week 9: Advanced Processing**
- Specialized algorithms and techniques
- Performance optimization case studies
- **Files:** 1.py, 2.py, 2.sh (batch processing)

### **Week 10: Optimization Challenges**
- Complex performance problems
- Algorithm optimization strategies
- **Files:** 1.py, 2.py

### **Week 11: Batch Job Scheduling**
- Advanced BSUB job array syntax
- Parallel job execution patterns
- Wait and synchronization mechanisms
- **Files:** 1_array.sh, 2_array.sh, 3_wait.sh, 4_any_reason.sh

### **Week 13: Matrix Multiplication & Final Topics**
- Optimized matrix multiplication
- Performance analysis
- **Files:** matmul.py, 1.sh

---

## Key Topics Covered

- **NumPy**: arrays, linear algebra, broadcasting, vectorization
- **Parallel Computing**: multiprocessing, process pools, distributed algorithms
- **Performance Optimization**: profiling, memory management, algorithm design
- **Large Data**: memory mapping, chunked processing, Zarr format
- **HPC Job Scheduling**: BSUB job arrays, batch processing, resource management
- **Case Studies**: Mandelbrot set, matrix operations, geographical computing

---

## Technologies & Tools

- **Python 3**: Core language
- **NumPy**: Numerical computing and array operations
- **Matplotlib**: Visualization
- **Multiprocessing**: Parallel execution
- **Zarr**: Chunked array storage
- **Pandas**: Data manipulation
- **BSUB**: Job scheduling (DTU HPC environment)
- **Conda**: Dependency management

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

## Getting Started

### Prerequisites
- Python 3.7+
- NumPy, Matplotlib, Pandas
- Conda environment manager
- Access to HPC cluster (for BSUB scripts) or local terminal

### Setup
```bash
# Activate conda environment (if available)
conda activate 02613

# Navigate to course directory
cd /path/to/Python\ and\ High-Performance\ Computing

# Run individual scripts
python Week_2/autolab_numpy_1.py
```

### Running Examples
Each week contains executable Python scripts and corresponding shell scripts:
```bash
# Python examples
python Week_5_6/mandelbrot.py

# Batch job submission (on HPC cluster)
bsub < Week_11/1_array.sh
```

---

## Learning Outcomes

By completing this course, you will:
- Master NumPy for numerical computing and array operations
- Design and implement parallel algorithms using Python
- Optimize Python code for performance-critical applications
- Handle large datasets efficiently using out-of-core techniques
- Schedule and manage HPC batch jobs effectively
- Apply these concepts to real-world computational problems

---

## Notes

- Many scripts are designed for DTU HPC environment (requires BSUB scheduler)
- Some exercises reference external datasets and autolab submissions
- Performance scripts expect specific hardware configurations
- NumPy binary files (.npy) and Zarr arrays included for data persistence

---

## License

Course materials for educational purposes. Adjust licensing as needed based on institutional requirements.
