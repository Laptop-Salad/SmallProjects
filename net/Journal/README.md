# Journal
The most basic command-line journal written in using .NET 8.

Created for the sole purpose of using the Singleton pattern.

## How to setup this project
Refer to the following to install and run dotnet for development: https://dotnet.microsoft.com/en-us/learn/dotnet/hello-world-tutorial/install

Not for development:
1. Install dotnet: https://dotnet.microsoft.com/en-us/learn/dotnet/hello-world-tutorial/install. Ignore the vscode section.
2. Check if dotnet is installed by running "dotnet"
3. Do: dotnet run inside the project directory.

## Create an entry
```
new <name of entry>
```

![alt text](screenshots/image.png)

## Write to an entry
```
write <name of existing entry>
```

![alt text](screenshots/image-2.png)

### Writing to a non-existent entry
![alt text](screenshots/image-3.png)

## Read an entry
```
read <name of existing entry>
```

![alt text](screenshots/image-1.png)

### Reading a non-existent entry

![alt text](screenshots/image-4.png)