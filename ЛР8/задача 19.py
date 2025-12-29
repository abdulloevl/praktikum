import time
import random
import os
import requests
import pandas as pd
import torch
import torch.nn as nn
import streamlit as st
from datetime import datetime

# =========================
# AI NEURAL NETWORK
# =========================
class CyberAI(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(4, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.net(x)

model = CyberAI()

# =========================
# TRAIN MODEL (SIMULATION)
# =========================
def train_ai():
    data = []
    labels = []

    for _ in range(800):
        amount = random.uniform(10, 500)
        hour = random.randint(8, 22)
        failed = random.randint(0, 1)
        ip_risk = 0
        data.append([amount, hour, failed, ip_risk])
        labels.append(0)

    for _ in range(200):
        amount = random.uniform(5000, 20000)
        hour = random.randint(0, 5)
        failed = random.randint(5, 10)
        ip_risk = 1
        data.append([amount, hour, failed, ip_risk])
        labels.append(1)

    X = torch.tensor(data, dtype=torch.float32)
    y = torch.tensor(labels, dtype=torch.float32).view(-1, 1)

    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    loss_fn = nn.BCELoss()

    for _ in range(300):
        optimizer.zero_grad()
        loss = loss_fn(model(X), y)
        loss.backward()
        optimizer.step()

train_ai()

# =========================
# FIREWALL IP BLOCK
# =========================
def block_ip(ip):
    os.system(f"iptables -A INPUT -s {ip} -j DROP")

# =========================
# GEOLOCATION
# =========================
def geo_ip(ip):
    try:
        r = requests.get(f"https://ipapi.co/{ip}/json/", timeout=3)
        j = r.json()
        return f"{j.get('country_name')} / {j.get('city')}"
    except:
        return "Unknown"

# =========================
# EVENT GENERATOR
# =========================
def generate_event():
    return {
        "amount": random.choice([50, 100, 300, 8000, 15000]),
        "hour": datetime.now().hour,
        "failed": random.randint(0, 10),
        "ip_risk": random.choice([0, 0, 0, 1]),
        "ip": f"45.{random.randint(10,200)}.{random.randint(1,255)}.{random.randint(1,255)}"
    }

# =========================
# STREAMLIT DASHBOARD
# =========================
st.set_page_config(page_title="Bank Cyber AI", layout="wide")
st.title("🔐 Bank Cyber AI – Anti‑Hack & Anti‑Fraud System")

log_table = []

if "logs" not in st.session_state:
    st.session_state.logs = []

while True:
    event = generate_event()
    x = torch.tensor([[event["amount"], event["hour"], event["failed"], event["ip_risk"]]])
    risk = model(x).item()

    geo = geo_ip(event["ip"])
    status = "SAFE"

    if risk > 0.7 or event["failed"] > 5 or event["ip_risk"] == 1:
        status = "🚨 ATTACK"
        block_ip(event["ip"])

    st.session_state.logs.append({
        "Time": datetime.now().strftime("%H:%M:%S"),
        "IP": event["ip"],
        "Geo": geo,
        "Amount": event["amount"],
        "Failed logins": event["failed"],
        "Risk score": round(risk, 2),
        "Status": status
    })

    df = pd.DataFrame(st.session_state.logs[-30:])

    st.subheader("📊 Real‑Time Security Monitor")
    st.dataframe(df, use_container_width=True)

    time.sleep(1)
    st.experimental_rerun()
