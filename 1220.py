import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import math

# Streamlit 页面标题
st.title("Damped Oscillation Visualization")

# 用户输入
mass = st.slider('Mass (kg)', min_value=0.1, max_value=0.25, value=0.25, step=0.01)
amplitude = st.slider('Amplitude (m)', min_value=0.01, max_value=0.1, value=0.1, step=0.01)
thickness = st.slider('Thickness (mm)', min_value=2.0, max_value=10.0, value=1.0, step=0.1)
height = st.slider('Height (m)', min_value=0.01, max_value=0.08, value=0.08, step=0.01)
spring_constant = st.slider('Spring constant (N/m)', min_value=10, max_value=20, value=1, step=1)

# 计算参数
T = (2*math.pi*(mass/spring_constant)**0.5)  # 周期
k = 0.000002991722221
b = k * (height ** -3) * (mass ** -0.75) * (np.e ** (-0.263/thickness))

# 生成图表
fig, ax = plt.subplots(figsize=(8, 5))
ax.set_title('Y-T Plot')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Displacement (m)')
ax.grid(True)

# 动态数据
time_values = np.linspace(0, 15, 1500)
displacement_values = amplitude * np.exp(-b * time_values) * np.cos(2 * np.pi * time_values / T)
ax.plot(time_values, displacement_values, label="Displacement")
ax.legend()

# 显示图表
st.pyplot(fig)
