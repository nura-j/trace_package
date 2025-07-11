from setuptools import setup
import os

PKG_ROOT = os.path.abspath(os.path.dirname(__file__))


def load_requirements():
    with open(os.path.join(PKG_ROOT, "requirements.txt"), encoding="utf-8") as f:
        all_reqs = f.read().splitlines()

    install_requires = []

    for req in all_reqs:
        req = req.strip()
        if req and not req.startswith('#'):
            if req.startswith('git+'):
                # Convert Git URL to PEP 508 format
                # git+https://github.com/nura-j/ABSynth_dataset.git -> ABSynth_dataset @ git+https://...
                pkg_name = "absynth"
                install_requires.append(f"{pkg_name} @ {req}")
            else:
                install_requires.append(req)

    return install_requires


install_requires = load_requirements()

setup(
    name='trace',
    version='0.1',
    packages=[
        'trace',
        'trace.hessian',
        'trace.transformer',
        'trace.linguistic_probes',
        'trace.intrisic_dimensions',
        'trace.tokenizer',
        'trace.utils',
        'trace.dataloader',
        'trace.training',
        'trace.output_monitoring'
    ],
    url='https://github.com/nura-j/trace_package',
    license='GPLv3',
    author='Nura Aljaafari',
    author_email='nuraaljaafari@gmail.com',
    description='TRACE',
    install_requires=install_requires,
    python_requires=">=3.11",
)
