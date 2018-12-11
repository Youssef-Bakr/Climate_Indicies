import os

import numpy as np
import pytest

# constants
# start and end year of the monthly precipitation, temperature, and PET datasets
_DATA_YEAR_START_MONTHLY = 1895
_DATA_YEAR_END_MONTHLY = 2017

# start and end year of the calibration periods
# used by SPI/SPEI Pearson calculations
_CALIBRATION_YEAR_START_MONTHLY = 1981
_CALIBRATION_YEAR_END_MONTHLY = 2010
_CALIBRATION_YEAR_START_PALMER = 1931
_CALIBRATION_YEAR_END_PALMER = 1990

# start and end years relevant to the daily datasets
_DATA_YEAR_START_DAILY = 1998
_CALIBRATION_YEAR_START_DAILY = 1998
_CALIBRATION_YEAR_END_DAILY = 2016

# latitude value used for computing the fixture datasets (PET, Palmers)
_LATITUDE_DEGREES = 25.2292

# available water capacity value used for computing the fixture datasets (Palmers)
_AWC_INCHES = 4.5
_AWC_INCHES_PALMER = 5.0


@pytest.fixture(scope="module")
def data_year_start_monthly():
    return _DATA_YEAR_START_MONTHLY


@pytest.fixture(scope="module")
def data_year_end_monthly():
    return _DATA_YEAR_END_MONTHLY


@pytest.fixture(scope="module")
def data_year_start_daily():
    return _DATA_YEAR_START_DAILY


@pytest.fixture(scope="module")
def data_year_start_palmer():
    return _DATA_YEAR_START_MONTHLY


@pytest.fixture(scope="module")
def calibration_year_start_monthly():
    return _CALIBRATION_YEAR_START_MONTHLY


@pytest.fixture(scope="module")
def calibration_year_end_monthly():
    return _CALIBRATION_YEAR_END_MONTHLY


@pytest.fixture(scope="module")
def calibration_year_start_daily():
    return _CALIBRATION_YEAR_START_DAILY


@pytest.fixture(scope="module")
def calibration_year_start_palmer():
    return _CALIBRATION_YEAR_START_PALMER


@pytest.fixture(scope="module")
def calibration_year_end_palmer():
    return _CALIBRATION_YEAR_END_PALMER


@pytest.fixture(scope="module")
def calibration_year_end_daily():
    return _CALIBRATION_YEAR_END_DAILY


@pytest.fixture(scope="module")
def latitude_degrees():
    return _LATITUDE_DEGREES


@pytest.fixture(scope="module")
def awc_inches():
    return _AWC_INCHES


@pytest.fixture(scope="module")
def palmer_awc():
    return _AWC_INCHES_PALMER


@pytest.fixture(scope="module")
def precips_mm_monthly():

    return np.load("fixture/precips_mm_monthly.npy")


@pytest.fixture(scope="module")
def precips_mm_daily():

    return np.load("fixture/precips_mm_daily.npy")


@pytest.fixture(scope="module")
def transformed_pearson3():

    return np.load("fixture/pearson3_monthly.npy")


@pytest.fixture(scope="module")
def transformed_pearson3_monthly_fullperiod():

    return np.load("fixture/pearson3_monthly_full.npy")


@pytest.fixture(scope="module")
def transformed_gamma_monthly():
    """
    Array of values corresponding to the precips_mm_monthly array, i.e. those
    values have been transformed/fitted using an application of the gamma
    conversion/fitting algorithm provided in compute.py.

    :return:
    """
    return np.load("fixture/gamma_monthly.npy")


@pytest.fixture(scope="module")
def transformed_gamma_daily():
    """
    Array of values corresponding to the precips_mm_daily array, i.e. those
    values have been transformed/fitted using an application of the gamma
    conversion/fitting algorithm provided in compute.py.

    :return:
    """

    return np.load("fixture/gamma_daily.npy")


@pytest.fixture(scope="module")
def pet_thornthwaite_mm():

    return np.load("fixture/pet_thornthwaite.npy")


@pytest.fixture(scope="module")
def temps_celsius():

    return np.load("fixture/temp_celsius.npy")


@pytest.fixture(scope="module")
def pnp_6month():

    return np.load("fixture/pnp_06.npy")


@pytest.fixture(scope="module")
def spei_6_month_gamma():

    return np.load("fixture/spei_06_gamma.npy")


@pytest.fixture(scope="module")
def spei_6_month_pearson3():

    return np.load("fixture/spei_06_pearson3.npy")


@pytest.fixture(scope="module")
def spi_1_month_gamma():

    return np.load("fixture/spi_01_gamma.npy")


@pytest.fixture(scope="module")
def spi_6_month_gamma():

    return np.load("fixture/spi_06_gamma.npy")


@pytest.fixture(scope="module")
def spi_6_month_pearson3():

    return np.load("fixture/spi_06_pearson3.npy")


@pytest.fixture(scope="module")
def palmer_pet():

    return np.load("fixture/palmer_pet.npy")


@pytest.fixture(scope="module")
def palmer_precip():

    return np.load("fixture/palmer_precip.npy")


@pytest.fixture(scope="module")
def palmer_et():

    return np.load("fixture/palmer_et.npy")


@pytest.fixture(scope="module")
def palmer_pr():

    return np.load("fixture/palmer_pr.npy")


@pytest.fixture(scope="module")
def palmer_r():

    return np.load("fixture/palmer_r.npy")


@pytest.fixture(scope="module")
def palmer_ro():

    return np.load("fixture/palmer_ro.npy")


@pytest.fixture(scope="module")
def palmer_pro():

    return np.load("fixture/palmer_pro.npy")


@pytest.fixture(scope="module")
def palmer_l():

    return np.load("fixture/palmer_l.npy")


@pytest.fixture(scope="module")
def palmer_pl():

    return np.load("fixture/palmer_pl.npy")


@pytest.fixture(scope="module")
def palmer_pdsi_monthly():

    return np.load("fixture/palmer_pdsi.npy")


@pytest.fixture(scope="module")
def palmer_phdi_monthly():

    return np.load("fixture/palmer_phdi.npy")


@pytest.fixture(scope="module")
def palmer_pmdi_monthly():

    return np.load("fixture/palmer_pmdi.npy")


@pytest.fixture(scope="module")
def palmer_zindex():

    return np.load("fixture/palmer_zindex_0.npy")


@pytest.fixture(scope="module")
def palmer_alpha():

    return np.load("fixture/palmer_alpha.npy")


@pytest.fixture(scope="module")
def palmer_beta():

    return np.load("fixture/palmer_beta.npy")


@pytest.fixture(scope="module")
def palmer_gamma():

    return np.load("fixture/palmer_gamma.npy")


@pytest.fixture(scope="module")
def palmer_delta():

    return np.load("fixture/palmer_delta.npy")


@pytest.fixture(scope="module")
def palmer_K():

    return np.load("fixture/palmer_k.npy")


@pytest.fixture(scope="module")
def palmer_zindex_monthly():

    return np.load("fixture/palmer_zindex_1.npy")


@pytest.fixture(scope="module")
def palmer_scpdsi_monthly():

    return np.load("fixture/palmer_scpdsi.npy")


@pytest.fixture(scope="module")
def palmer_scphdi_monthly():

    return np.load("fixture/palmer_scphdi.npy")


@pytest.fixture(scope="module")
def palmer_scpmdi_monthly():

    return np.load("fixture/palmer_scpmdi.npy")


@pytest.fixture(scope="module")
def palmer_sczindex_monthly():

    return np.load("fixture/palmer_sczindex.npy")
