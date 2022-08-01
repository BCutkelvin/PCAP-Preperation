# - - - - - - - SECTION 1: MODULES AND PACKAGES - - - - - - -
# - - - - - - - PCAP-31-03 1.1 - Import and use modules and packages - - - - - - -

# 3)The import Statement

try:
    import nonExistentModule
except ImportError as ie:
    print(f"FAIL! - Module not found {ie}")
