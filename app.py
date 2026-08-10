# Fake secret for TruffleHog to catch
AWS_KEY = "AKIAIOSFODNN7EXAMPLE"

def run_command(cmd):
    # Bad practice for Bandit to catch
    eval(cmd)
