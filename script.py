class script(object):

    START_TEXT = """Hello,
i am Telegram URL Upload Bot! Created by @shreevish
Please send me any direct download URL Link, i can upload to telegram as File/Video
 🚨 . . . Note : its support almost all direct Url's except torrent link & some links . . . 🚨
 
🚨 PRON video🔞 Links gives you PERMANENT BAN 🚨
       ┈┈┈••💙✿❤️✿💚••┈┈┈
       
URL-UPLOADER bot created by @shreevish"""


    HELP_USER = """<b>Hai, Follow these steps..</b>
 
NOTE: Download may take some time! So please wait for it to complete!

1. Send url (Link|New Name with Extension).
2. Send Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots
   
Creator : @shreevish"""


    ABOUT_TEXT = """⭕️<b>My Name : URL-UPLOADER</b>
⭕️<b>Creater :</b> @shreevish
⭕️<b>Language :</b> <code>Python3</code>
⭕️<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 
⭕️<b>Source Code :</b> 👉 <a href='https://telegram.dog/All_Movie_rockers'>Click Here</a>"""



    FORMAT_SELECTION = """<b>Choose appropriate option</b> <a href='{}'>⬇️</a>
🎞  - Stream format
📁  - File format
<i>NOTE : Taking high resolutions may result in files above 2GB and hence cannot Upload to TG. So better select a medium resolution.</i> 😇
"""    
    
    UPGRADE_TEXT = "PING at @shreevish"
    
    DOWNLOAD_START = "Downloading to my server 📥 Please wait...⏳ 🙇🙇🙇 it takes time depend on File Size"
    
    UPLOAD_START = "Yay,File Download Successfully 😊 Now Uploading to Telegram 📤"
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."

    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "**Thank you for Using Meh!! ❤️**\nJoin @All_Movie_Rockers"
    
    SAVED_CUSTOM_THUMB_NAIL = "<b>✅Custom thumbnail Saved.\nThis thumbnail will be Permanent for all future uploads\n\nDo /delthumb to clear your thumbnail!</b>"
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom Thumbnail cleared succesfully."
    
    SHOW_THUMB = "@All_Movie_Rockers\n\nUse /delthumb to clear this thumbnail."
    
    NO_THUMB = "SED😕 No saved thumbnails Found!!"
    
    CUSTOM_CAPTION_UL_FILE = "<b>{newname}\n\n©️ @All_Movie_Rockers</b>"
    
    TIMEOUT = "<b><i>Sorry for the delay. It'll help reduce the flood wait</i> 😇\n\nWait for {} sec and try again.</b>"
