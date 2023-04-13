import pandas as pd
import numpy as np


chat_id = 460411293 # Ваш chat ID, не меняйте название переменной

def solution(control_sales, control_apps, test_sales, test_apps, alpha=0.04):
  
  control_conversion = control_sales / control_apps

 
  expected_sales = control_conversion * test_apps

  
  std_dev = math.sqrt(expected_sales * (1 - control_conversion))

 
  z_score = (test_sales - expected_sales) / std_dev

  
  critical_value = abs(stats.norm.ppf(alpha / 2))

  
  if abs(z_score) > critical_value:
    return True # Reject the null hypothesis
  else:
    return False # Fail to reject the null hypothesis

