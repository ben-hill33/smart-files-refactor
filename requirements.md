# Software Requirements

## What is the vision of this product?

- We want to create a app that takes all downloaded files and automatically puts them in the proper folder based on the file type. For example, an image (.jpg or .png) would automatically go into the images folder from downloads.

## What pain point does this project solve?

- Are you tired of having to organize your downloads manually? Do you just not have time for it? Our app will do this automatically so that the only thing you need to do is download. Our app will automatically filter it into the correct directory.

## Why should we care about your product?

- No one likes digging through a whole bunch of files to find what they are looking for and it's not fun to take time daily to organize these files. Smart Files does it all for you.

  #### IN

  - Should sort your downloaded files into 1 of 4 directories(Media, Documents, Software and Other)
  - Shold be able to run Smart Files on an ad hoc basis
  - Defaults to run Smart Files daily using crontab
  - Should be downloadable via pip
  - Work for MacOS users

  #### OUT

  - Sort files not in the downloads folder
  - Work on Windows computers

### Minimum Viable Product (MVP)

- We will be able to _easily_ prove that common file types for images, videos, standard docs, and software downloads will automatically transfer from the downloads folder to the correct directory. Our app should be able to do this in a very short amount of time to display seamless functionality. In addition, the app should be able to work on all our individual machines. This app will be added as a pip module. This will involve at least:

- Creating a setup file to help new users download and use as intended.

- Creating various forms of documentation.

- Creating a license.

- Creating a source distribution (meta-data) to ensure program works on everyone’s computer.
- Testing and publishing package on PyPl.

### Stretch Goals

- Option for organizing screenshots
- Break down folders into sub folders i.e. Documents will be broken down into text files, word documents, excel file etc.
- Allow user to choose how often they want Smart Files to run in crontab (Every minute, Every hour, every month)
- Available for Windows users

## Functional Requirements

1. User can run the app on an ad hoc basis

### Data Flow

- Install Smart Files via `pip`
- Update $PATH
- Source file
- Smart file will now be set up in crontabs to run daily
- type `smart-file run` to run smart file on an ad hoc basis

## Non-Functional Requirements

1. Usability: This is important because we dont want to this app to be harder than just having the user sort the files themselves. This will be implemented by having a seemless command line interface and easy to run commands.

2. Reliability: No one will want to use this app if it breaks all the time. We want to make sure we are catching all errors and displaying them to the user in a way thats is easy to understand and easy to fix.
