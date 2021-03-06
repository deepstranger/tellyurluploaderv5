class Translation(object):
    START_TEXT = """Hello,
I am Fastest URL Uploader Bot! Developed by @Tellybots_4u

Please send me any direct download URL Link, i can upload to telegram as File/Video

Tellyurluploader bot by @Tellybots_4u"""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "Contact @sahaynitin815 for Details"
    FORMAT_SELECTION = """๐ญ ๐ฆ๐ฒ๐น๐ฒ๐ฐ๐ ๐๐ป๐ฑ ๐๐ต๐ผ๐๐ฒ ๐ฌ๐ผ๐๐ฟ ๐๐ผ๐ฟ๐บ๐ฎ๐๐

๐๏ธ ๐ฉ๐๐๐๐ข = Upload as Streamable.

๐ ๐๐๐๐ = Upload as File.
โขโขโขโขโขโขโขโขโขโขโขโขโขโขโขโขโขโขโข

โผ/delthumbnail = To Delete thumbnail

โผPlease send photo to save Thumbnail before you press any Below Button

๐ฒPowered By: @Tellybots_4u."""
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos Follow the steps :-

โฒFor Custom Name
โผURL | FileName.Extension

โฒFor Premium Videos
โผURL | FileName.Extension | username | password"""
    NOYES_URL = "Unknown URL detected. Use an Another Url"
    DOWNLOAD_START = "Downloading to my server \n๐ฅ Please wait...โณ โกโก \nIt takes time depend on File Size"
    UPLOAD_START = "Yay,File Download Successfully ๐ \nNow Uploading to Telegram ๐ค"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). \nNeverthless, Yay,File Download Successfully ๐  \nNow Uploading to Telegram ๐ค."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2 GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Thanks for using me. \nDownloaded in {} seconds. \nJoin : @Tellybots_4u . \nUploaded in {} seconds."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Thanks for using me. \nDownloaded in {} seconds. \nJoin : @Tellybots_4u . \nUploaded in {} seconds"
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/tellybots_support'>Tellybots_4u</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. \nThis image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "โ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "โ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    NO_VOID_FORMAT_FOUND = "Sorry, Your link doesnot cointain any video\n<b>YouTubeDL</b> said: {}\nFor More Contact @tellybots_support"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """โญ๏ธ<b>My Name : Telly-URL-Uploader</b>
โญ๏ธ<b>Developer :</b> @Tellybots_4u
โญ๏ธ<b>Language :</b> <code>Python3</code>
โญ๏ธ<b>Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram 1.0.7</a> 
โญ๏ธ<b>Source Code :</b> ๐ <a href='https://telegram.dog/tellybots_4u'>Click Here</a>"""
    
    HELP_USER = """Hi I am URL Uploader bot..
๐  Follow the below steps to download :-

1. Send url (Link|New Name with Extension).
2. Send Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots
   
Developer : @Tellybots_4u

Contact @sahaynitin815 for getting premium subscription

Support Group : ยฉ @Tellybots_support"""
 
        
        
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\nยฉ @tellybots_4u"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/FFMpegRoBot"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. โ?๏ธ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """ """
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    SHOW_THUMB = "Use /deletethumbnail to clear this thumbnail."
    NO_THUMB = "No saved thumbnails Found!!\n\nSend an image to save it as your thumbnail permanently."

