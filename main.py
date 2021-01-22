import gspread

gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("theSocialGamePokerclub").sheet1

# Update a range of cells using the top left corner address
# wks.update('A1', [[1, 2], [3, 4]])
next_tweet = wks.acell('A2').value

#post tweet through twitterAPI

#delete row on success
wks.delete_rows(2)

# Or update a single cell
# wks.update('B42', "it's down there somewhere, let me take another look.")

# Format the header
# wks.format('A1:B1', {'textFormat': {'bold': True}})