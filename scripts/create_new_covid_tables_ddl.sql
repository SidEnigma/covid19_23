CREATE TABLE covid_reporting.new_cases_and_deaths
(
    country                 VARCHAR(100),
    country_code_2_digit    VARCHAR(2),
    country_code_3_digit    VARCHAR(3),
    population              BIGINT,
    cases_count             BIGINT,
    deaths_count            BIGINT,
    year_week               VARCHAR(10),
    source                  VARCHAR(500)
)
GO

CREATE TABLE covid_reporting.new_hospital_admissions_weekly
(
    country                 VARCHAR(100),
    country_code_2_digit    VARCHAR(2),
    country_code_3_digit    VARCHAR(3),
    population              BIGINT,
    reported_year_week      VARCHAR(10),
    reported_week_start_date DATE,
    reported_week_end_date   DATE,
    new_hospital_admissions_count BIGINT,
    new_icu_admissions_count      BIGINT,
    source                  VARCHAR(500)
)
GO
