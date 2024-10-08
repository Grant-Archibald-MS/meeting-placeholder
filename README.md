# Meeting Placeholder

In situations where you need to cancel a Microsoft Teams call but still want to engage with your users. In this sitiation option option that you can consider is to the RTMP In option of Microsoft Teams to present placeholder content. This approach frees you up from having to present a screen with a predefined message during the meeting.

This setup allows you to maintain engagement with your audience even when you can't interactively attend the meeting in person.

## Sample Code

This repository provides a solution to stream images or videos as placeholder content during your scheduled Teams meetings.

## Approach

1. **Update Teams Call to Enable RTMP In**
   - Configure your Teams meeting to accept RTMP In streams.
   - Refer to [Use RTMP-In in Microsoft Teams - Microsoft Support](https://support.microsoft.com/office/use-rtmp-in-in-microsoft-teams-789d6090-8511-4e2e-add6-52a9f551be7f)

2. **Ensure `ffmpeg` and `python` is Installed**
   - Install `ffmpeg` using the following command in a Linux:

     ```sh
     sudo apt install ffmpeg python3 python3-pip
     ```

3. **Install Python Dependencies**

   - Install the required Python packages:
     ```sh
     pip3 install -r requirements.txt
     ```

4. **Run the Script**
   - Execute the script to start streaming placeholder content:

     ```sh
     python3 meeting.py
     ```

## Usage

1. **Prepare Your Content**
   - Place your images or videos in the specified folder.

2. **Start Streaming**
   - Run the script and provide the RTMPS URL and stream key when prompted.

3. Review and adjust the streaming rate which has a default value of 100k by default

