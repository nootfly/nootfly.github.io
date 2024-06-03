---
layout: post
title: "Flutter Github workflow"
date: 2024-06-03 11:20:00 +1000
categories: tech
tags: github tools
---



### How to Use `actions/upload-artifact@v2`

Here’s a step-by-step guide to using `actions/upload-artifact@v2` in your GitHub Actions workflow:

1. **Set Up Your Workflow File:**
   Create a `.yml` file in the `.github/workflows` directory of your repository. For example, `ci.yml`.

2. **Add the Upload Artifact Step:**
   Add the `actions/upload-artifact@v2` step to your workflow to specify which files or directories to upload.

### Example Workflow

Below is a complete example of a GitHub Actions workflow that installs dependencies, runs tests, generates a coverage report, and then uploads the coverage report as an artifact:

```yaml
name: Flutter CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Install Flutter
        uses: subosito/flutter-action@v1
        with:
          flutter-version: '2.2.0'

      - name: Install Dependencies
        run: flutter pub get

      - name: Run Tests with Coverage
        run: flutter test --coverage

      - name: Generate Coverage Report
        run: |
          sudo apt-get install lcov
          genhtml -o coverage coverage/lcov.info

      - name: Upload Coverage Report
        uses: actions/upload-artifact@v2
        with:
          name: coverage-report
          path: coverage
```

### Breakdown of the Example Workflow

1. **Checkout Code:**
   ```yaml
   - uses: actions/checkout@v2
   ```

   This step checks out your repository code so that the workflow can access it.

2. **Install Flutter:**
   ```yaml
   - name: Install Flutter
     uses: subosito/flutter-action@v1
     with:
       flutter-version: '2.2.0'
   ```

   This step installs the specified version of Flutter.

3. **Install Dependencies:**
   ```yaml
   - name: Install Dependencies
     run: flutter pub get
   ```

   This step runs `flutter pub get` to install all the project dependencies.

4. **Run Tests with Coverage:**
   ```yaml
   - name: Run Tests with Coverage
     run: flutter test --coverage
   ```

   This step runs your tests and generates a coverage report in the `coverage` directory.

5. **Generate Coverage Report:**
   ```yaml
   - name: Generate Coverage Report
     run: |
       sudo apt-get install lcov
       genhtml -o coverage coverage/lcov.info
   ```

   This step installs `lcov` and generates an HTML coverage report from the `lcov.info` file.

6. **Upload Coverage Report:**
   ```yaml
   - name: Upload Coverage Report
     uses: actions/upload-artifact@v2
     with:
       name: coverage-report
       path: coverage
   ```

   This step uses the `actions/upload-artifact@v2` action to upload the contents of the `coverage` directory as an artifact named `coverage-report`.

### Accessing Uploaded Artifacts

After the workflow runs, you can download the uploaded artifact from the "Actions" tab in your GitHub repository:

1. Go to the "Actions" tab.
2. Select the workflow run that you are interested in.
3. In the summary of the workflow run, you will see a section labeled "Artifacts".
4. Click on the artifact name (e.g., `coverage-report`) to download it.

This allows you to preserve and share important files generated during your workflow.