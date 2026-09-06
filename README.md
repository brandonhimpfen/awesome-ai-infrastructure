# Awesome AI Infrastructure [![Awesome Lists](https://srv-cdn.himpfen.io/badges/awesome-lists/awesomelists-flat.svg)](https://github.com/brandonhimpfen/awesome-lists)

[![Support Open Work](https://img.shields.io/badge/Support-Open%20Work-0A0A0A?style=flat&logo=github)](https://github.com/brandonhimpfen/support) 
[![GitHub Sponsor](https://srv-cdn.himpfen.io/badges/github/github-flat.svg)](https://github.com/sponsors/brandonhimpfen) 
[![Buy Me a Coffee](https://srv-cdn.himpfen.io/badges/buymeacoffee/buymeacoffee-flat.svg)](https://buymeacoffee.com/brandonhimpfen) 
[![Ko-Fi](https://srv-cdn.himpfen.io/badges/kofi/kofi-flat.svg)](https://ko-fi.com/brandonhimpfen) 
[![PayPal](https://srv-cdn.himpfen.io/badges/paypal/paypal-flat.svg)](https://www.paypal.com/donate/?hosted_button_id=3LLKRXJU44EJJ) <br />
[![X](https://srv-cdn.himpfen.io/badges/twitter/twitter-flat.svg)](https://x.com/ListsAwesome) 
[![Facebook](https://srv-cdn.himpfen.io/badges/facebook-pages/facebook-pages-flat.svg)](https://www.facebook.com/awesomelists)

> A curated list of awesome tools, frameworks, platforms, and resources for building scalable and efficient AI infrastructure, including distributed training, model serving, MLOps, and deployment.

## Contents

- [Distributed Training](#distributed-training)
- [Model Serving and Deployment](#model-serving-and-deployment)
- [MLOps and Automation](#mlops-and-automation)
- [Data Management](#data-management)
- [Optimization Tools](#optimization-tools)
- [Infrastructure as Code](#infrastructure-as-code)
- [Cloud Platforms](#cloud-platforms)
- [Learning Resources](#learning-resources)
- [Books](#books)
- [Community](#community)
- [Contribute](#contribute)
- [License](#license)

## Distributed Training

- [Horovod](https://horovod.ai/) - A distributed deep learning training framework for TensorFlow, Keras, and PyTorch.
- [Ray](https://www.ray.io/) - A framework for building scalable distributed applications, including distributed AI and reinforcement learning.
- [PyTorch Distributed](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html) - Tools and libraries for distributed training in PyTorch.
- [DeepSpeed](https://www.deepspeed.ai/) - A deep learning optimization library that makes distributed training easy and efficient.
- [MPI for Machine Learning](https://www.mpich.org/) - Using the Message Passing Interface (MPI) standard for distributed machine learning.

## Model Serving and Deployment

- [TensorFlow Serving](https://www.tensorflow.org/tfx/guide/serving) - A flexible, high-performance serving system for machine learning models.
- [TorchServe](https://pytorch.org/serve/) - A model serving framework for PyTorch, providing fast and efficient model deployment.
- [NVIDIA Triton Inference Server](https://developer.nvidia.com/nvidia-triton-inference-server) - A scalable model serving platform supporting multiple frameworks.
- [ONNX Runtime](https://onnxruntime.ai/) - A cross-platform, high-performance scoring engine for serving ONNX models.
- [Seldon Core](https://www.seldon.io/tech/products/core/) - An open-source platform for deploying and monitoring machine learning models on Kubernetes.
- [KFServing (KServe)](https://kserve.github.io/website/) - A Kubernetes-based model serving solution as part of the Kubeflow project.

## MLOps and Automation

- [MLflow](https://mlflow.org/) - An open-source platform for managing the end-to-end machine learning lifecycle.
- [Kubeflow](https://www.kubeflow.org/) - A platform for orchestrating machine learning workflows on Kubernetes.
- [DVC (Data Version Control)](https://dvc.org/) - A tool for version control and reproducibility in machine learning projects.
- [ZenML](https://zenml.io/) - An extensible MLOps framework for creating portable, production-ready machine learning pipelines.
- [Airflow](https://airflow.apache.org/) - A platform for orchestrating complex workflows, commonly used in machine learning pipelines.
- [Metaflow](https://metaflow.org/) - A human-centric framework for building and managing real-life data science projects, developed by Netflix.

## Data Management

- [Delta Lake](https://delta.io/) - An open-source storage layer that brings reliability to data lakes.
- [Apache Hudi](https://hudi.apache.org/) - A data management framework that simplifies incremental data processing and streaming analytics.
- [Feast](https://feast.dev/) - An open-source feature store for managing and serving machine learning features.
- [Great Expectations](https://greatexpectations.io/) - A tool for data validation and testing in machine learning workflows.
- [LakeFS](https://lakefs.io/) - An open-source data versioning platform for managing data lakes.

## Optimization Tools

- [NVIDIA TensorRT](https://developer.nvidia.com/tensorrt) - A high-performance deep learning inference optimizer and runtime.
- [Apache TVM](https://tvm.apache.org/) - A deep learning compiler stack for optimizing models on various hardware backends.
- [Intel OpenVINO](https://docs.openvino.ai/latest/index.html) - A toolkit for optimizing and deploying AI inference on Intel hardware.
- [OctoML](https://octoml.ai/) - An AI model optimization platform for efficient deployment on edge and cloud.
- [Quantization Aware Training (QAT)](https://www.tensorflow.org/model_optimization) - Tools for optimizing model performance through quantization.

## Infrastructure as Code

- [Terraform](https://www.terraform.io/) - A tool for building, changing, and versioning infrastructure safely and efficiently.
- [Pulumi](https://www.pulumi.com/) - Infrastructure as code for deploying and managing cloud infrastructure using programming languages.
- [Ansible](https://www.ansible.com/) - An open-source automation tool for provisioning and managing infrastructure.
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/) - A service for automating AWS resource deployment and management.
- [Google Deployment Manager](https://cloud.google.com/deployment-manager) - An infrastructure management tool for Google Cloud Platform.

## Cloud Platforms

- [AWS SageMaker](https://aws.amazon.com/sagemaker/) - A comprehensive platform for building, training, and deploying machine learning models on AWS.
- [Google AI Platform](https://cloud.google.com/ai-platform) - Google Cloud’s integrated environment for AI development and deployment.
- [Azure Machine Learning](https://azure.microsoft.com/en-us/services/machine-learning/) - A cloud-based platform for training, deploying, and managing machine learning models.
- [IBM Watson Studio](https://www.ibm.com/cloud/watson-studio) - A suite of tools for data science, machine learning, and AI model development.
- [Paperspace Gradient](https://gradient.paperspace.com/) - A cloud platform for developing, training, and deploying machine learning models.
- [KubeStellar Console](https://github.com/kubestellar/console) - A CNCF Sandbox multi-cluster Kubernetes management dashboard for deploying and observing workloads across edge and cloud infrastructure.

## Learning Resources

- [Coursera: MLOps Fundamentals](https://www.coursera.org/specializations/mlops-fundamentals) - A course on MLOps best practices for machine learning projects.
- [Google Cloud: ML Operations](https://cloud.google.com/learn/training/ai-ml-operations) - Training resources on MLOps and model deployment.
- [AWS SageMaker Workshops](https://sagemaker-examples.readthedocs.io/en/latest/) - Example projects and tutorials for using AWS SageMaker.
- [Kubeflow Documentation](https://www.kubeflow.org/docs/) - Official documentation and guides for using Kubeflow.
- [PyTorch Distributed Training Guide](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html) - A tutorial on distributed training with PyTorch.

## Books

- [Machine Learning Engineering](https://tinyurl.com/yphttdp2) by Andriy Burkov - A book on building scalable machine learning infrastructure.
- [Building Machine Learning Powered Applications](https://tinyurl.com/36d66dwk) by Emmanuel Ameisen - A guide to building robust ML applications in production.
- [Designing Data-Intensive Applications](https://tinyurl.com/y74fyb66) by Martin Kleppmann - A comprehensive guide to building scalable and reliable data systems.
- MLOps: Data Science in Production by Mark Treveil and The Dotscience Team - A book on best practices for MLOps and model deployment.
- [Reliable Machine Learning](https://tinyurl.com/4ezxcbm9) by Cathy Chen - A book on creating resilient machine learning infrastructure.

## Community

- [MLOps Community](https://mlops.community/) - A global community focused on MLOps and AI infrastructure.
- [Reddit: r/MachineLearning](https://www.reddit.com/r/MachineLearning/) - A subreddit for discussions on machine learning infrastructure and tools.
- [Kubeflow Slack](https://kubeflow.slack.com/) - A Slack community for discussing Kubeflow and machine learning pipelines.
- [Paperspace Forums](https://forums.paperspace.com/) - A community forum for discussing machine learning infrastructure and tools.
- [GitHub: MLOps Repositories](https://github.com/topics/mlops) - A collection of open-source MLOps projects on GitHub.

## Contribute

Contributions are welcome. Please ensure your submission fully follows the requirements outlined in [`CONTRIBUTING.md`](CONTRIBUTING.md), including formatting, scope alignment, and category placement.

Pull requests that do not adhere to the contribution guidelines may be closed.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/)

*This awesome list contains affiliate links.*
