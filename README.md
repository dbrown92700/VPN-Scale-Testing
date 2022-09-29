# VPN-Scale-Testing

These scripts create vManage templates for VPN Scale testing.
- mail.py will generate feature templates.  It uses the settings in includes.py.
- cliConfig.py will generate a CLI template.  It uses the settings in cliincludes.py
- both scripts use the settings in vmanage_credentials.py.
- both scrips rely on one or more template variables in their includes files that have the framework of the device, vpn, subinterface, etc. templates. Those templates have variables in them delineated as ~~~variable~~~ that the script uses to inject the scaled VPN definitions.  If you use the feature template scripts, you will have to redefine the templates since they have several object references specific to the system this was built on. To do that, I recommend building starter templates in the specific test vManage and using the Swagger interface to pull the JSON definitions.  The feature templates are under Configuration - General Template, Get /template/feature.  Device templates are under Configuration - Template Mastertemplate/device to get the templateId and Configuration - Template Master, Get /template/device/object/{templateId} to get the full JSON definition.
- cliConfig.py script generates a list of addresses to use when attaching the config to a device, or you can use the generateAddresses.py script to get them
