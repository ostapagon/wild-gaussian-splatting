from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
import subprocess

# Helper function to execute commands
def install_dependencies():
    print("Installing dependencies...")

        cuda_home = subprocess.getoutput('echo $CUDA_HOME')
    print(f"CUDA Path: {cuda_home}")

    # Print nvcc version
    try:
        nvcc_version = subprocess.getoutput('nvcc --version')
        print("nvcc Version:")
        print(nvcc_version)
    except FileNotFoundError:
        print("nvcc is not installed or not in PATH.")

    # Print PyTorch version and CUDA compatibility
    try:
        import torch
        print('PyTorch Version:', torch.__version__)
        print('CUDA Available:', torch.cuda.is_available())
        if torch.cuda.is_available():
            print('CUDA Version:', torch.version.cuda)
            print('CUDA Device Count:', torch.cuda.device_count())
            print('CUDA Device Name:', torch.cuda.get_device_name(0))
    except ImportError:
        print("PyTorch is not installed.")

    # subprocess.run(["pip", "install", "-r", "dust3r/requirements.txt"], check=True)
    # subprocess.run(["pip", "install", "-r", "dust3r/requirements_optional.txt"], check=True)
    # subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)


    # Compile RoPE positional embeddings
    # subprocess.run(["python", "dust3r/croco/models/curope/setup.py", "build_ext", "--inplace"], check=True)

    # Download pre-trained models
    # subprocess.run(["mkdir", "-p", "dust3r/checkpoints"], check=True)
    # subprocess.run([
    #     "wget",
    #     "https://download.europe.naverlabs.com/ComputerVision/DUSt3R/DUSt3R_ViTLarge_BaseDecoder_512_dpt.pth",
    #     "-P",
    #     "dust3r/checkpoints/"
    # ], check=True)
    # subprocess.run(["mkdir", "-p", "mast3r/checkpoints"], check=True)
    # subprocess.run([
    #     "wget",
    #     "https://download.europe.naverlabs.com/ComputerVision/MASt3R/MASt3R_ViTLarge_BaseDecoder_512_catmlpdpt_metric.pth",
    #     "-P",
    #     "mast3r/checkpoints/"
    # ], check=True)

    # Install additional editable packages
    subprocess.run(["pip", "install", "-e", "gaussian-splatting/submodules/diff-gaussian-rasterization"], check=True)
    subprocess.run(["pip", "install", "-e", "gaussian-splatting/submodules/simple-knn"], check=True)

class CustomInstallCommand(install):
    """Customized setuptools install command - runs install_dependencies."""
    def run(self):
        install_dependencies()
        super().run()  # Call the standard install process

class CustomDevelopCommand(develop):
    """Customized setuptools develop command - runs install_dependencies."""
    def run(self):
        install_dependencies()
        super().run()  # Call the standard develop process

# Define the setup
setup(
    name='wild-gaussian-splatting',
    version='0.1.0',
    description='Setup script for Wild Gaussian Splatting environment and dependencies.',
    packages=find_packages(),
    install_requires=[
        'ipywidgets>=8.0.2',
        'jupyterlab==3.4.2',
        'lovely-tensors==0.1.15',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
    },
)
