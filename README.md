# Lecture Video Repository

## Introduction
This repository is dedicated to storing and accessing video recordings of lectures via Git Large File Storage (LFS) to ensure efficient handling of large media files.

## Setup Instructions

### Prerequisites
- Git: Install from [https://git-scm.com/downloads](https://git-scm.com/downloads)
- Git LFS: Install from [https://git-lfs.github.com/](https://git-lfs.github.com/)

### Cloning and Configuration
Clone the repository and set up Git LFS by running the following commands in your terminal:

```bash
# Clone the repository
git clone https://github.com/tuanngocfun/human-character-detection.git
cd human-character-detection

# Install Git LFS and pull files
git lfs install
git lfs pull

# Switch to the lectures branch
git checkout lectures
