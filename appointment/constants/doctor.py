"""
Degrees Associated With Doctors
"""


class DoctorDegrees:
    # Primary medical degrees
    BACHELOR_OF_MEDICINE = 'MBBS'
    DOCTOR_OF_MEDICINE = 'MD'
    DOCTOR_OF_OSTEOPATHIC_MEDICINE = 'DO'

    # Higher medical degrees
    DOCTOR_OF_MEDICINE_BY_RESEARCH = 'MDRes'
    DOCTOR_OF_PHILOSOPHY = 'PhD'

    # Other degrees
    MASTER_OF_CLINICAL_MEDICINE = 'MCM'
    MASTER_OF_MEDICAL_SCIENCE = 'MMSc'
    MASTER_OF_MEDICINE = 'MM'
    MASTER_OF_PHILOSOPHY = 'MPhil'
    MASTER_OF_SURGERY = 'MSurg'
    MASTER_OF_SCIENCE_IN_MEDICINE = 'MSc'
    DOCTOR_OF_CLINICAL_MEDICINE = 'DCM'
    DOCTOR_OF_CLINICAL_SURGERY = 'DClinSurg'
    DOCTOR_OF_MEDICAL_SCIENCE = 'DMSc'
    DOCTOR_OF_SURGERY = 'DS'


DOCTOR_DEGREE_OPTIONS = (
    (DoctorDegrees.BACHELOR_OF_MEDICINE, 'Bachelor of Medicine / Bachelor of Surgery (MBBS, BMBS, MBChB, MBBCh)'),
    (DoctorDegrees.DOCTOR_OF_MEDICINE, 'Doctor of Medicine (MD, Dr.MuD, Dr.Med)'),
    (DoctorDegrees.DOCTOR_OF_OSTEOPATHIC_MEDICINE, 'Doctor of Osteopathic Medicine (DO)'),
    (DoctorDegrees.DOCTOR_OF_MEDICINE_BY_RESEARCH, 'Doctor of Medicine by research (MD(Res), DM)'),
    (DoctorDegrees.DOCTOR_OF_PHILOSOPHY, 'Doctor of Philosophy (PhD, DPhil)'),
    (DoctorDegrees.MASTER_OF_CLINICAL_MEDICINE, 'Master of Clinical Medicine (MCM)'),
    (DoctorDegrees.MASTER_OF_MEDICAL_SCIENCE, 'Master of Medical Science (MMSc, MMedSc)'),
    (DoctorDegrees.MASTER_OF_MEDICINE, 'Master of Medicine (MM, MMed)'),
    (DoctorDegrees.MASTER_OF_PHILOSOPHY, 'Master of Philosophy (MPhil)'),
    (DoctorDegrees.MASTER_OF_SURGERY, 'Master of Surgery (MS, MSurg, MChir, MCh, ChM, CM)'),
    (DoctorDegrees.MASTER_OF_SCIENCE_IN_MEDICINE, 'Master of Science in Medicine or Surgery (MSc)'),
    (DoctorDegrees.DOCTOR_OF_CLINICAL_MEDICINE, 'Doctor of Clinical Medicine (DCM)'),
    (DoctorDegrees.DOCTOR_OF_CLINICAL_SURGERY, 'Doctor of Clinical Surgery (DClinSurg)'),
    (DoctorDegrees.DOCTOR_OF_MEDICAL_SCIENCE, 'Doctor of Medical Science (DMSc, DMedSc)'),
    (DoctorDegrees.DOCTOR_OF_SURGERY, 'Doctor of Surgery (DS, DSurg)'),
)