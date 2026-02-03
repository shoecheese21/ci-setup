# Smart CI Reporter 🚀

A custom CI pipeline built using GitHub Actions that automatically:
- Runs unit tests
- Generates a markdown test report
- Uploads reports as artifacts
- Publishes results directly in the GitHub Actions Summary

## 🔧 Tech Stack
- Python
- Pytest
- GitHub Actions

## 📊 Features
- Automated CI on push & PR
- Test result visibility inside Actions UI
- Downloadable test reports
- Clean, reusable workflow

## ▶️ How to Run Locally
```bash
pip install -r requirements.txt
pytest
