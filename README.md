# RaiBlocks-Python
This API lets you connect to your Rai Wallet such that you can access the ledger. Some of the code is based on SergiySW's RaiWalletBot code which you can find here: https://github.com/SergiySW/RaiWalletBot

Requires:

- python-requests
- local wallet node


How to use:

- Make sure your config.json in C:\Users\YOURUSERNAME\AppData\Local\RaiBlocksfile has correct port and that
"rpc_enabled" is true.

Example:

- raiRichList.py gives the accumulated percentage of the richlist found at https://raiblocks.net/page/frontiers.php
- detective.py gives a list of all transactions that has received a 100 000 NANO deposit or more from one of Bitgrail's two addresses
