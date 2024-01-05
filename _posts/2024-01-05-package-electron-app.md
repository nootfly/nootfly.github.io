---
layout: post
title: "Package Electron app to wrap a website"
date: 2024-01-05 13:00:00 +1100
categories: tech
tags: web tools
---


## Set up the project

 Electron is a framework that allows for the development of native applications with web technologies like JavaScript, HTML, and CSS, and it provides various features to create a kiosk mode application. Here's a basic outline of how you can achieve this:

### 1. Set Up Your Electron Project

First, you need to set up an Electron project if you haven't already. You can do this by initializing a new Node.js project and installing Electron. For example:

```bash
mkdir my-kiosk-app
cd my-kiosk-app
npm init -y
npm install electron --save-dev
```

### 2. Create Your Main File

Create a main file for your Electron application, typically named `main.js`. This file will create and control your application window.

### 3. Configure the BrowserWindow

In your `main.js`, you'll need to import Electron and create a `BrowserWindow` that loads your website. You can enable kiosk mode by setting the `kiosk` property to `true` in the `BrowserWindow` options. For example:

```javascript
const { app, BrowserWindow } = require('electron');

function createWindow() {
    const win = new BrowserWindow({
        fullscreen: true,
        kiosk: true,
        frame: false, // This enables kiosk mode
        webPreferences: {
            nodeIntegration: true
        }
    });

    win.loadURL('http://www.example.com'); // Load your website
}

app.whenReady().then(createWindow);
```

### 4. Run Your Application

Run your application with Electron. If you've set everything up correctly, it should open in full screen (kiosk mode), displaying your website. Use the following command to run the Electron application:

```bash
npx electron .
```

### Additional Considerations:

- **Security:** Ensure that your application is secure, especially if it's going to be used in a public setting.
- **Customization:** You can customize the Electron window further to suit your needs. For example, you might want to disable the menu bar, enable or disable certain web features, etc.
- **Exiting Kiosk Mode:** Consider how you will allow users to exit kiosk mode if necessary. This might involve listening for a certain key combination or implementing a hidden exit button.
- **Handling Offline Scenarios:** If your kiosk application relies on a website, make sure to handle scenarios where the internet connection might be unstable or unavailable.
- **Updating Content:** Plan how you'll update the website or application content as needed, perhaps through remote updates or scheduled maintenance.

Using Electron for kiosk applications can be quite powerful, as it combines the simplicity of web technology with the capabilities of native applications.


## Package the project


Here's a basic guide using `electron-packager`, which is straightforward and widely used:

### Step 1: Install Electron Packager

First, you need to install `electron-packager` globally or as a dev dependency in your project. To install it as a dev dependency, run:

```bash
npm install electron-packager --save-dev
```

### Step 2: Package Your Application

Once installed, you can use `electron-packager` to package your application. Run the following command in your project's root directory:

```bash
npx electron-packager . MyKioskApp --platform=win32 --arch=x64 --out=release-builds
```

- Replace `MyKioskApp` with the desired name for your application.
- The `--platform=win32` option specifies Windows as the target platform.
- The `--arch=x64` specifies the architecture (use `ia32` for 32-bit).
- The `--out` option specifies the output directory for the packaged application.

### Step 3: Locate the Packaged Application

After running the command, `electron-packager` will create a directory named `release-builds` (or whatever you specified) in your project directory. Inside, you'll find the packaged app with a `.exe` executable file, which can be run on Windows.

### Additional Options and Customization:

- **Icon**: You can add an application icon by using the `--icon` flag with a path to an `.ico` file.
- **Additional Resources**: If your app uses additional files or resources, you can include them in the package.
- **Custom Scripts**: You can write custom scripts in your `package.json` file to simplify the packaging process.

### Alternatives:

- **Electron Builder**: This is another popular tool for packaging and also supports auto-updating, code signing, and more.
- **Electron Forge**: It provides a more comprehensive set of utilities for the development, packaging, and distribution process.

Remember, after packaging, it's essential to thoroughly test the .exe file on different systems to ensure it runs correctly and without issues. Packaging also doesn't handle code signing and distribution, which are additional steps you may need to consider for a public release.
