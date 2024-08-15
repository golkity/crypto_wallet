from aiohttp import request
from flask import Flask, jsonify, render_template, session

from web3 import Web3

import requests

import json

app = Flask(__name__)
infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(infura_url))
app.config['SECRET_CODE'] = 'твой сексретный код'

