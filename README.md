
# eit scripts
This readme serves to give a brief explanation on the different scripts that exists in this folder.

1. export_records.py ~ Backup
This python script is used to take a backup of the screening and enrolled databases in redcap.
This script is ran by a cronjob on the eit server that runs once daily. The data is exported using a json file format.

2. import_records.py ~ Database Restore/Data Import
This python script is used to restore a backup that was previously taken. It can also be used for a data import.There are two things
that need to be taken changed on the script before running it, to indicate the correct file name of the backup (or import file) to be restored and the token of the database to be backed up. The script expects to import a json file format.

3. subject_identifier.py ~ Create Screening Bids
This python script is used to generate screening bids. The Bids are of the format S-XX-YYYY-ZZ where S is used to indicate it is a screening bid, XX is used to indicate the clinician number, YYYY is the sequence and ZZ is the check digit using modulus 97. What needs to be changed is the start and stop range, they are usually done in batches of 100 for each clinician.

4. verify_bids.py ~ Verify BIDS
This python script is used to verify that screening bids and enrolled bids correspond to what was generated through the script and EDC respectively.

5. lab_result_value_correctness.py ~ Verify result correctness
This python script is used compare each result item for hematology, cd4-cd8, viral load, chemistry for infant and maternal. It checks the entered values against the rounded values from dmis.

6. redcap_backup.sh ~ cronjob backup script
This script is ran by a cronjob to backup the redcap databases.
