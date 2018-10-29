NAME = 'RNA CCLE Large Intestine'

UPLOAD_TO_PLOTLY = False

FEATURE_X_SAMPLE_FILE_PATH = '../data/rna__gene_x_cell_line.colon_cancer.tsv'

NANIZE = 0

DROP_NA_AXIS = 1

MAX_NA = 0.05

MIN_N_NOT_NA_UNIQUE_VALUE = None

SHIFT_AS_NECESSARY_BEFORE_LOGGING = '0<'

LOG_BASE = '2'

NORMALIZATION_AXIS = 0

NORMALIZATION_METHOD = '-0-'

SELECT_GENE_SYMBOLS = True

FEATURES_TO_PEEK = ()

SAMPLES_TO_PEEK = ()

SCALE_WITH_KL = True

MAX_N_JOB = 1

SELECT_CONTEXT = 'both'

FEATURES_FILE_PATH = None

SELECT_FEATURE_AUTOMATICALLY = True

N_TOP_FEATURE = None

NMF_KS = tuple(range(
    2,
    10,
))

NMF_K = 6

HCC_KS = NMF_KS

WT_HCC_K = NMF_K

H_HCC_K = NMF_K

EXTREME_FEATURE_THRESHOLD = 8

ELEMENT_ENTROPY_QUANTILE = 1

GPS_MAP_WT_PULL_POWER = 2.4

GPS_MAP_WT_ELEMENT_MARKER_SIZE = 8

GPS_MAP_WT_BANDWIDTH_FACTOR = 6.4

GPS_MAP_H_PULL_POWER = 1.6

GPS_MAP_H_ELEMENT_MARKER_SIZE = 24

GPS_MAP_H_BANDWIDTH_FACTOR = 6.4
