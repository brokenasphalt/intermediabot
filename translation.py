# File Name     - Translation
# Description   - Text translation file
# Owner         - Kiddilan
# Repo          - https://github.com/m4mallu
# Tg Uid        - @kiddilan
# Channel       - @MovieKeralam
# ---------------------------------------------------------------------------------------- #

class Translation(object):
    NOT_AUTH_TXT = "⚠️ <b>Unauthorized Access</b> ⚠️\n<code>You are not in Auth Users List.  So you can't use the core " \
                   "components of this bot. Inconvenience is regretted !</code> "
    DOWNLOAD_START = "📥<b>DOWNLOAD BEGIN</b>📥<i> Plz wait..</i>"
    UPLOAD_START = "📤<b>UPLOAD BEGIN</b>📤<i> Plz wait..</i>"
    SAVED_CUSTOM_THUMB_NAIL = "<b>✅ Thumbnail Saved Successfully.</b>\n<code>This file will be used in upcoming " \
                              "rename or video conversions</code> "
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared successfully."
    SAVED_RECVD_DOC_FILE = "<b>✔️File Downloaded Successfully</b>\n⏱<code>Give the required file name with " \
                           "extension.Eg:</code><b>Terminator.mkv</b><code> as a reply to this message</code> "
    ACCESS_DENIED_TEXT = "You are not authorized to use this Bot."
    START_TEXT = "Hello.. {}\n\n<b>This is a new version file converter bot</b>\n\n1️⃣ <code>In order to set a custom thumbnail " \
                 "for the process, forward an image to the bot. The thumbnail will remain unchanged until you clear " \
                 "it in the <b>Options</b> tab. Except this, videos won't have thumbnails.</code>\n\n2️⃣ <code>Forward a telegram " \
                 "media to the bot.</code>\n\n3️⃣ <code>Reply to the media with the command</code> <b>/download</b> <code>and follow the " \
                 "instructions.</code>\n\n4️⃣ <code>Bot will output your formatted media with custom thumbnail, screenshots and a " \
                 "sample video.</code>\n\n<b>Credits- <a href='https://t.me/kiddilan'>@admin</a></b> "
    SETTINGS_TEXT = "<b>These are my available options:</b>"
    THUMB_CAPTION = "<code>This image is your current thumbnail, Tap</code><b> DEL THUMB </b><code>if you wish to " \
                    "clear it !</code> "
    NO_THUMB = "⛔️ <b>There are no thumbnails in your local directory.</b>\n<code>Please upload an image to save it " \
               "!</code> "
    DEL_CUSTOM_THUMB_NAIL = "✅ <b>Thumbnail cleared successfully.</b>\n<code>Thumbnail won't be available to the " \
                            "downloading media, unless you upload an image !</code> "
    DEL_THUMB_CONFIRM = "⚠️ <b>Do you want to remove thumbnail?</b>\n<code>Thumbnail won't be available in the videos " \
                        "when you delete it!</code> "
    LONG_FILE_NAME = "File Name limit allowed by Telegram is {alimit} characters!\nThe given file name has {num} " \
                     "characters.<b>LONGER FILENAMES AREn'T ALLOWED</b> Please short your file name and try again! "
    FILE_TYPE_SELEC = "Select the file type for\n<b>File name:</b>{}"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>Please wait: </b> 😉\nFor some Screenshots & sample video.<code> Usually it " \
                                  "will take 30Sec. to upload it. Please be patient...</code>"
    INPUT_MEDIA = "<b>Can I download this media for conversion?</b>"
    INPUT_ERROR = "<b>⚠️ Invalid input:</b>️\n<code>Input the file name as replay to the above message and " \
                  "check the supported extensions in welcome message !</code> "
    EXTENSIONS = ['.mkv', '.mp4', '.avi', '.webm']
    NO_SPAM_MSG = "⚠️ <b>Don't Spam Here</b>\n<code>Read the welcome message for better use of this bot !</code>"
    CAPTION_TEXT = "@moviekeralam"
    THANKS_MESSAGE = "<b>Thanks for using.Have a nice day</b>💕"
    MAKE_A_COPY_TEXT = "📚 <b> Can i make a copy of the same ?</b>"
    FINISHED_PROGRESS_STR = "◼️"
    UN_FINISHED_PROGRESS_STR = "◻️"
    FAILED_LINK = "<b>Failed To Fetch Youtube Data...</b>\n<code>Please try again after some time.If " \
                  "problem persists, May be your server IP got blocked by the YouTube </code>😔 "
    PROCESS_START = "Processing Youtube Url 🔎 🔎 🔎"

    CUSTOM_CAPTION_DOC = "━━━━━━━━━ ✧ ━━━━━━━━\n&ensp;💢<a href='https://t.me/MoviekeralamLinks'>@MoviekeralamLinks</a" \
                         ">💢\n━━━━━━━━━ ✧ ━━━━━━━━\n\n🎗<b>ʝσιи🎗ѕнαяє🎗ѕυρρσят</b>🎗 "
    CUSTOM_CAPTION_VIDEO = "🏷:\n\n&ensp;&ensp;&ensp; 🎞 <b>STREAMABLE FILE</b> 🎞\n\n&ensp;&ensp;&ensp;💢<a " \
                           "href='https://t.me/MoviekeralamLinks'>@MoviekeralamLinks</a>💢 "
    BOT_PM_TEXT = "<b>PM from:</b>\nName:&ensp;<b>{}</b>\nUser Name:&ensp;@{}\nUser Id:&ensp;{}\nBot Name:&ensp;<b>{" \
                  "}</b>\nBot Username:&ensp;@{} "
    BOT_RN_TEXT = "<b>Rename from:</b>\nName:&ensp;<b>{}</b>\nUser Name:&ensp;@{}\nUser Id:&ensp;{}\nBot " \
                  "Name:&ensp;<b>{}</b>\nBot Username:&ensp;@{} "
    BOT_CV_TEXT = "<b>Video Conversion from:</b>\nName:&ensp;<b>{}</b>\nUser Name:&ensp;@{}\nUser Id:&ensp;{}\nBot " \
                  "Name:&ensp;<b>{}</b>\nBot Username:&ensp;@{} "
