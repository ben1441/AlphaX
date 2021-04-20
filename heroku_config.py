import os

class var(object):
  "APP_ID" = int(os.environ.get("APP_ID", 6))
  # 6 is a placeholder
  "API_HASH" = os.environ.get("API_HASH", "b00e27babc25c281d2ec18242b5b6760")
  "STRING_SESSION" = os.environ.get("STRING_SESSION", None)
  "BOT_TOKEN" = os.environ.get("BOT_TOKEN", None)
  "BOT_USERNAME" = os.environ.get("BOT_USERNAME", None)
  "HEROKU_KEY" = os.environ.get("HEROKU_KEY", None)
  "HEROKU_APP_NAME" = os.environ.get("HEROKU_APP_NAME", None)
  "DATABASE_URI" = os.environ.get("DATABASE", None)
  "DATABASE_NAME" = os.environ.get("DATABASE_NAME", None)
  "ALIVE_PIC" = os.environ.get("ALIVE_PIC", None)
  "ALIVE_NAME" = os.environ.get("ALIVE_NAME", None)
  "PMPERMIT_PIC" = os.environ.get("PMPERMIT_PIC", None)
  "PRIVATE_GROUP_ID" = os.environ.get("PRIVATE_GROUP_ID", None)
      if PRIVATE_GROUP_ID != None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError("Invalid Private Group ID. Make sure your ID is starts with -100----------")


class Development(Var):
    LOGGER = True
    # Here for later codes...