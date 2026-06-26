import time

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# =========================================================
# PAGE SETTINGS
# =========================================================
st.set_page_config(
    page_title="기본소득 × 청년 위기 분석 허브",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# HIGH-CONTRAST STYLE
# =========================================================
st.markdown(
    """
    <style>
    :root {
        --bg: #0F1117;
        --sidebar: #111827;
        --card: #1E2235;
        --card2: #172033;
        --text: #F8FAFC;
        --muted: #CBD5E1;
        --soft: #E2E8F0;
        --blue: #4F8CFF;
        --orange: #FFB020;
        --green: #32D583;
        --purple: #A78BFA;
        --red: #F97066;
    }

    .stApp {
        background: var(--bg);
        color: var(--text);
    }

    section[data-testid="stSidebar"] {
        background-color: var(--sidebar);
        border-right: 1px solid rgba(255,255,255,0.10);
    }

    section[data-testid="stSidebar"] * {
        color: var(--text) !important;
        opacity: 1 !important;
    }

    p, li, label, span, div[data-testid="stMarkdownContainer"] {
        color: var(--text) !important;
        opacity: 1 !important;
    }

    div[data-testid="stCaptionContainer"] {
        color: var(--muted) !important;
        font-weight: 650 !important;
        opacity: 1 !important;
    }

    /* Selectbox / dropdown contrast fix */
    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] * {
        color: #111827 !important;
        opacity: 1 !important;
        font-weight: 700 !important;
    }

    div[data-baseweb="select"] input {
        color: #111827 !important;
        -webkit-text-fill-color: #111827 !important;
    }

    div[data-baseweb="popover"],
    div[data-baseweb="popover"] * {
        color: #111827 !important;
        background-color: #FFFFFF !important;
        opacity: 1 !important;
    }

    div[role="listbox"],
    div[role="option"],
    div[role="option"] * {
        color: #111827 !important;
        background-color: #FFFFFF !important;
        opacity: 1 !important;
        font-weight: 700 !important;
    }

    div[role="option"]:hover,
    div[role="option"]:hover * {
        background-color: #E5E7EB !important;
        color: #111827 !important;
    }

    .main-title {
        font-size: clamp(2rem, 5vw, 3.1rem);
        font-weight: 950;
        line-height: 1.12;
        letter-spacing: -0.045em;
        margin: 0.2rem 0 0.4rem 0;
        background: linear-gradient(90deg, #4F8CFF 0%, #FFB020 34%, #32D583 66%, #A78BFA 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .sub-title {
        color: #E2E8F0;
        font-size: 1.08rem;
        font-weight: 650;
        margin-bottom: 1.15rem;
    }

    .question-box {
        background: linear-gradient(135deg, rgba(79,140,255,0.25), rgba(167,139,250,0.18));
        border: 1px solid rgba(79,140,255,0.65);
        border-radius: 18px;
        padding: 18px 20px;
        margin: 14px 0 24px 0;
        font-size: 1.12rem;
        font-weight: 850;
        color: #FFFFFF;
        box-shadow: 0 10px 28px rgba(0,0,0,0.22);
    }

    .card {
        background: var(--card);
        border: 1px solid rgba(255,255,255,0.16);
        border-radius: 18px;
        padding: 18px;
        box-shadow: 0 12px 34px rgba(0,0,0,0.26);
        min-height: 132px;
    }

    .kpi-label {
        color: #E2E8F0;
        font-size: 0.92rem;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .kpi-value {
        font-size: 2.05rem;
        font-weight: 950;
        margin-bottom: 4px;
    }

    .kpi-note {
        color: #CBD5E1;
        font-size: 0.82rem;
        font-weight: 650;
    }

    .section-title {
        font-size: 1.48rem;
        font-weight: 950;
        margin: 22px 0 12px 0;
        color: #FFFFFF;
        letter-spacing: -0.025em;
    }

    .mini-caption {
        color: #CBD5E1;
        font-size: 0.83rem;
        font-weight: 650;
        margin-top: -4px;
        margin-bottom: 16px;
    }

    .scenario-banner {
        background: rgba(255,176,32,0.16);
        border: 1px solid rgba(255,176,32,0.70);
        color: #FFF4D6;
        padding: 15px 17px;
        border-radius: 16px;
        font-weight: 850;
        margin-bottom: 18px;
    }

    .insight-box {
        background: #121826;
        border: 1px solid rgba(79,140,255,0.52);
        border-radius: 16px;
        padding: 17px 19px;
        color: #F8FAFC;
        line-height: 1.72;
        font-size: 1rem;
        font-weight: 600;
        margin-top: 12px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.24);
    }

    .policy-card {
        background: var(--card);
        border-left: 5px solid var(--blue);
        border-top: 1px solid rgba(255,255,255,0.13);
        border-right: 1px solid rgba(255,255,255,0.13);
        border-bottom: 1px solid rgba(255,255,255,0.13);
        border-radius: 16px;
        padding: 18px;
        height: 100%;
        color: #F8FAFC;
        font-weight: 600;
        line-height: 1.62;
    }

    .creator-card {
        background: #172033;
        border: 1px solid rgba(255,255,255,0.20);
        border-radius: 14px;
        padding: 14px 16px;
        line-height: 1.8;
        font-weight: 850;
        color: #FFFFFF;
        box-shadow: 0 8px 22px rgba(0,0,0,0.18);
    }

    .footer {
        margin-top: 36px;
        padding: 20px;
        border-top: 1px solid rgba(255,255,255,0.14);
        color: #CBD5E1;
        font-size: 0.86rem;
        font-weight: 600;
        line-height: 1.65;
    }

    div[data-testid="stMetric"] {
        background-color: var(--card);
        padding: 17px;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.16);
        box-shadow: 0 8px 26px rgba(0,0,0,0.20);
    }

    div[data-testid="stMetric"] label,
    div[data-testid="stMetric"] div {
        color: #F8FAFC !important;
        font-weight: 850 !important;
        opacity: 1 !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        flex-wrap: wrap;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #1E2235;
        border-radius: 999px;
        padding: 10px 18px;
        color: #F8FAFC !important;
        font-weight: 850;
        border: 1px solid rgba(255,255,255,0.12);
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #4F8CFF, #A78BFA) !important;
        color: white !important;
        border-bottom: 3px solid #FF4D5E !important;
    }

    .stRadio label p,
    .stSlider label,
    .stToggle label p,
    .stSelectbox label p {
        color: #F8FAFC !important;
        font-weight: 850 !important;
        opacity: 1 !important;
    }

    button[kind="secondary"] p,
    button p {
        color: #FFFFFF !important;
        font-weight: 850 !important;
    }

    .js-plotly-plot .plotly .main-svg text {
        fill: #F8FAFC !important;
        opacity: 1 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# LANGUAGE
# =========================================================
st.sidebar.markdown("### 🌐 Language")
language_choice = st.sidebar.radio(
    "Choose display language",
    ["한국어", "English"],
    horizontal=True,
    label_visibility="collapsed",
)
LANG = "ko" if language_choice == "한국어" else "en"

TEXT = {
    "ko": {
        "title": "기본소득 × 청년 실업·주거 위기 분석 허브",
        "subtitle": "사회복지와 경영경제 관점으로 청년 위기와 기본소득 정책을 함께 분석하는 인터랙티브 대시보드",
        "question": "기본소득은 청년 실업과 주거 위기의 해법이 될 수 있을까?",
        "overview": "개요",
        "welfare": "사회복지 분석",
        "business": "경영경제 분석",
        "simulation": "🎮 가상 시뮬레이션",
        "policy": "정책 제언",
        "year_select": "연도 선택",
        "youth_unemp": "청년실업률",
        "housing_burden": "청년 주거부담률",
        "ubi_cases": "기본소득 실험·논의 사례 수",
        "welfare_spend": "한국 공공사회복지지출 비율",
        "source_note": "출처: KOSIS, OECD Data, 한국은행, 공공 정책 보고서 기반 교육용 재구성",
        "simulation_note": "이 시뮬레이션은 가상 시나리오 기반입니다",
        "monthly_amount": "기본소득 월 지급액",
        "target": "지급 대상",
        "youth_only": "청년 19~34세 한정",
        "all_people": "전 국민",
        "funding": "재원 조달 방식",
        "tax": "증세",
        "debt": "국채",
        "merge": "기존 복지 통합",
        "voucher": "청년 주거 바우처 포함",
        "ai_sim": "이 설정으로 AI 스타일 해석받기",
        "last_scenario": "내가 설정한 시나리오 기준 정책 제언",
        "short_term": "단기",
        "mid_term": "중기",
        "long_term": "장기",
        "chart_source": "자료: 공공 통계 기반 교육용 재구성, 시뮬레이션 값은 가상 모델",
        "case_title": "기본소득 실험 사례 카드",
        "ai_welfare": "사회복지 관점 인사이트 생성",
        "ai_business": "경영경제 관점 인사이트 생성",
        "ai_policy": "통합 정책 제언 생성",
        "data_warning": "실제 통계와 가상 시뮬레이션을 분리해 해석해야 합니다",
        "project_note": "한국어 기본 / English toggle",
        "created_by": "제작 및 기획",
        "footer": "이 대시보드는 월간 게시판 탐구 프로젝트를 위한 교육용 분석 허브입니다 실제 정책 예측이나 공식 통계 발표가 아니며, 모든 시뮬레이션 결과는 단순화된 가정에 기반합니다",
    },
    "en": {
        "title": "Basic Income × Youth Unemployment & Housing Crisis Hub",
        "subtitle": "An interactive dashboard connecting social welfare and business-economics perspectives on youth insecurity and basic income policy",
        "question": "Can basic income become a realistic solution to youth unemployment and housing insecurity?",
        "overview": "Overview",
        "welfare": "Social Welfare Analysis",
        "business": "Business & Economic Analysis",
        "simulation": "🎮 Virtual Simulation",
        "policy": "Policy Recommendations",
        "year_select": "Select year",
        "youth_unemp": "Youth unemployment rate",
        "housing_burden": "Youth housing burden rate",
        "ubi_cases": "Basic income experiment/discussion cases",
        "welfare_spend": "Korea public social spending ratio",
        "source_note": "Sources: Educational reconstruction based on KOSIS, OECD Data, Bank of Korea, and public policy reports",
        "simulation_note": "This simulation is based on hypothetical scenarios",
        "monthly_amount": "Monthly basic income amount",
        "target": "Payment target",
        "youth_only": "Youth only, ages 19–34",
        "all_people": "All citizens",
        "funding": "Funding method",
        "tax": "Tax increase",
        "debt": "Government debt",
        "merge": "Welfare integration",
        "voucher": "Include youth housing voucher",
        "ai_sim": "Get AI-style interpretation",
        "last_scenario": "Policy recommendation based on my selected scenario",
        "short_term": "Short term",
        "mid_term": "Mid term",
        "long_term": "Long term",
        "chart_source": "Source: Educational reconstruction based on public statistics; simulation values are hypothetical",
        "case_title": "Basic income experiment case cards",
        "ai_welfare": "Generate social welfare insight",
        "ai_business": "Generate business-economics insight",
        "ai_policy": "Generate integrated policy recommendation",
        "data_warning": "Actual statistics and hypothetical simulation outputs should be interpreted separately",
        "project_note": "Korean-first dashboard / English toggle included",
        "created_by": "Planned & Created by",
        "footer": "This dashboard is an educational analysis hub for a monthly board research project It is not an official forecast or statistical publication, and all simulation results are based on simplified assumptions",
    },
}
T = TEXT[LANG]


# =========================================================
# DATA
# =========================================================
years = [2019, 2020, 2021, 2022, 2023, 2024]

main_df = pd.DataFrame(
    {
        "year": years,
        "youth_unemployment": [8.9, 9.0, 7.8, 6.4, 5.9, 5.9],
        "housing_burden": [21.2, 22.1, 23.8, 25.1, 26.4, 27.2],
        "ubi_case_count": [4, 5, 6, 7, 8, 8],
        "welfare_spending": [12.2, 13.6, 15.2, 15.3, 15.5, 15.7],
    }
)

oecd_df = pd.DataFrame(
    {
        "country_ko": ["한국", "일본", "독일", "핀란드", "캐나다", "OECD 평균"],
        "country_en": ["Korea", "Japan", "Germany", "Finland", "Canada", "OECD average"],
        "youth_unemployment": [5.9, 4.2, 5.8, 15.7, 11.3, 13.0],
    }
)

funding_df = pd.DataFrame(
    {
        "method_ko": ["증세", "국채", "기존 복지 통합"],
        "method_en": ["Tax increase", "Government debt", "Welfare integration"],
        "fiscal_burden": [68, 82, 49],
        "political_risk": [73, 64, 58],
    }
)

consumption_df = pd.DataFrame(
    {
        "year": [2024, 2025, 2026, 2027, 2028],
        "low": [0.00, 0.18, 0.24, 0.28, 0.30],
        "medium": [0.00, 0.35, 0.48, 0.55, 0.58],
        "high": [0.00, 0.62, 0.78, 0.84, 0.86],
    }
)

sector_df = pd.DataFrame(
    {
        "sector_ko": ["보건·복지", "교육", "숙박·음식", "IT·정보통신", "제조업", "문화·콘텐츠", "금융·보험"],
        "sector_en": ["Health & welfare", "Education", "Accommodation & food", "IT & communication", "Manufacturing", "Culture & content", "Finance & insurance"],
        "youth_employment_rate": [52, 41, 47, 58, 49, 44, 39],
        "avg_wage": [280, 260, 220, 390, 330, 250, 410],
        "stability": [78, 72, 46, 70, 66, 52, 74],
    }
)

case_cards = {
    "ko": [
        {
            "title": "핀란드 기본소득 실험",
            "tag": "복지 안정성",
            "body": "실업자에게 조건 없는 현금 지원을 제공한 사례입니다 고용 효과는 제한적이었지만 심리적 안정감과 삶의 만족도 개선이 관찰됐다는 점에서 복지 효과 논의에 자주 활용됩니다",
        },
        {
            "title": "경기도 청년기본소득",
            "tag": "청년·지역경제",
            "body": "청년에게 정기적 지역화폐를 지급한 국내 사례입니다 청년의 소비 여력과 지역경제 순환을 함께 보는 정책 사례로 해석할 수 있습니다",
        },
        {
            "title": "캐나다 기본소득 논의",
            "tag": "빈곤 완화",
            "body": "기본소득 파일럿과 저소득층 소득보장 논의가 이어진 사례입니다 빈곤 완화와 노동시장 참여 사이의 균형을 분석하는 데 적합합니다",
        },
    ],
    "en": [
        {
            "title": "Finland Basic Income Experiment",
            "tag": "Welfare stability",
            "body": "This case provided unconditional cash support to unemployed participants Employment effects were limited, but welfare discussions often focus on psychological security and life satisfaction",
        },
        {
            "title": "Gyeonggi Youth Basic Income",
            "tag": "Youth & local economy",
            "body": "This Korean case offered regular local-currency payments to young adults It can be interpreted through both youth welfare and local consumption effects",
        },
        {
            "title": "Canada Basic Income Discussion",
            "tag": "Poverty reduction",
            "body": "Canadian policy debates offer a useful lens for analysing poverty reduction, income security, and labour market participation",
        },
    ],
}


# =========================================================
# HELPERS
# =========================================================
def apply_plotly_style(fig, height=380, title=None, x_title=None, y_title=None):
    fig.update_layout(
        template="plotly_dark",
        height=height,
        title=title,
        paper_bgcolor="#0F1117",
        plot_bgcolor="#0F1117",
        font={"color": "#F8FAFC", "size": 14},
        title_font={"color": "#FFFFFF", "size": 21},
        legend={"font": {"color": "#F8FAFC", "size": 13}},
        margin={"l": 45, "r": 30, "t": 70 if title else 35, "b": 45},
    )
    fig.update_xaxes(
        title=x_title,
        color="#F8FAFC",
        title_font={"color": "#FFFFFF", "size": 15},
        tickfont={"color": "#CBD5E1", "size": 13},
        gridcolor="rgba(226,232,240,0.24)",
        zerolinecolor="rgba(226,232,240,0.35)",
    )
    fig.update_yaxes(
        title=y_title,
        color="#F8FAFC",
        title_font={"color": "#FFFFFF", "size": 15},
        tickfont={"color": "#CBD5E1", "size": 13},
        gridcolor="rgba(226,232,240,0.24)",
        zerolinecolor="rgba(226,232,240,0.35)",
    )
    return fig


def card(label, value, note, color):
    st.markdown(
        f"""
        <div class="card">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value" style="color:{color};">{value}</div>
            <div class="kpi-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section(title):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)


def caption(text=None):
    st.markdown(f'<div class="mini-caption">{text or T["chart_source"]}</div>', unsafe_allow_html=True)


def insight_stream(text):
    placeholder = st.empty()
    shown = ""
    for ch in text:
        shown += ch
        placeholder.markdown(f'<div class="insight-box">{shown}▌</div>', unsafe_allow_html=True)
        time.sleep(0.003)
    placeholder.markdown(f'<div class="insight-box">{shown}</div>', unsafe_allow_html=True)


def funding_code(label):
    if label in ["증세", "Tax increase"]:
        return "tax"
    if label in ["국채", "Government debt"]:
        return "debt"
    return "merge"


def scenario_calculation(amount, target_label, funding_label, voucher_on):
    target_is_all = target_label in ["전 국민", "All citizens"]
    code = funding_code(funding_label)

    youth_population = 10.2
    total_population = 51.6
    population = total_population if target_is_all else youth_population

    annual_cost = amount * 10000 * 12 * population * 1_000_000 / 1_000_000_000_000
    annual_cost *= {"tax": 0.92, "debt": 1.05, "merge": 0.78}[code]

    amount_effect = amount * 0.014
    voucher_effect = 0.18 if voucher_on else 0
    target_effect = 0.12 if target_is_all else 0.24
    funding_penalty = {"tax": 0.08, "debt": 0.16, "merge": 0.11}[code]

    unemp_change = -(amount_effect + voucher_effect + target_effect) + funding_penalty
    projected_unemp = max(3.8, 5.9 + unemp_change)

    housing_drop = amount * 0.045 + (3.2 if voucher_on else 0)
    housing_burden = max(15.0, 27.2 - housing_drop)

    gdp_effect = amount * (0.008 if target_is_all else 0.0045)
    gdp_effect *= {"tax": 0.82, "debt": 1.04, "merge": 0.72}[code]
    gdp_effect = min(gdp_effect, 1.65)

    satisfaction = min(94, 45 + amount * 0.32 + (9 if voucher_on else 0) + (4 if not target_is_all else 0))
    fiscal_stability = max(18, 88 - annual_cost * 0.55 - (10 if code == "debt" else 0))
    feasibility = max(22, 82 - amount * 0.32 - (12 if target_is_all else 0) + (8 if code == "merge" else 0))

    return {
        "annual_cost": annual_cost,
        "unemp_change": unemp_change,
        "projected_unemp": projected_unemp,
        "housing_burden": housing_burden,
        "gdp_effect": gdp_effect,
        "satisfaction": satisfaction,
        "fiscal_stability": fiscal_stability,
        "feasibility": feasibility,
        "funding_code": code,
    }


def simple_ai_text(kind):
    if LANG == "ko":
        if kind == "welfare":
            return (
                "사회복지 관점에서 핵심은 청년실업률 자체보다 불안정한 고용, 높은 월세, 낮은 자산 형성이 동시에 겹친다는 점입니다<br><br>"
                "기본소득은 청년에게 최소한의 선택권과 시간 여유를 제공할 수 있지만, 주거비 상승이 빠른 상황에서는 현금 지원의 효과가 임대료로 흡수될 가능성도 있습니다<br><br>"
                "따라서 기본소득은 청년 공공임대, 주거 바우처, 고용 상담, 직업훈련과 연결될 때 복지 효과가 더 분명해집니다"
            )
        if kind == "business":
            return (
                "경영경제 관점에서 기본소득은 단기적으로 소비를 늘릴 수 있지만, 재원 조달 방식에 따라 파급효과가 크게 달라집니다<br><br>"
                "증세는 재정 안정성은 높지만 조세 저항이 생길 수 있고, 국채는 단기 수요 진작에는 유리하지만 장기 부담이 커질 수 있습니다<br><br>"
                "기업 입장에서는 청년층 소비 여력이 커지는 업종과 세금 부담이 커지는 업종이 다르게 나타나므로 산업별 영향 분석이 필요합니다"
            )
        return (
            "통합 정책 제언의 핵심은 전 국민 기본소득을 즉시 도입하기보다 청년층을 대상으로 한 제한적 실험부터 시작하는 것입니다<br><br>"
            "단기적으로는 청년 주거 바우처와 부분 기본소득을 결합하고, 중기적으로는 고용서비스와 지역 소비 효과를 측정해야 합니다<br><br>"
            "장기적으로는 재정 지속가능성, 기존 복지와의 중복, 조세 수용성을 검토한 뒤 단계적으로 확대하는 방식이 더 현실적입니다"
        )

    if kind == "welfare":
        return (
            "From a social welfare perspective, the key issue is not only youth unemployment itself, but the overlap of unstable work, high rent, and weak asset formation<br><br>"
            "Basic income may give young people minimum security and more room to make choices, but cash support can be absorbed by rising housing costs<br><br>"
            "Its welfare effect becomes clearer when it is linked with public rental housing, housing vouchers, employment counselling, and job training"
        )
    if kind == "business":
        return (
            "From a business-economics perspective, basic income can stimulate consumption in the short run, but the wider effect depends on the funding method<br><br>"
            "Tax increases may be fiscally stable but politically sensitive, while debt financing may create stronger short-term demand but larger long-term burdens<br><br>"
            "For businesses, the effects will differ by industry because some sectors benefit from youth consumption while others face higher tax pressure"
        )
    return (
        "The integrated recommendation is to begin with a limited youth-focused experiment rather than immediate universal basic income<br><br>"
        "In the short term, partial basic income should be combined with youth housing vouchers In the mid term, employment services and local consumption effects should be measured<br><br>"
        "In the long term, expansion should depend on fiscal sustainability, overlap with existing welfare programs, and public acceptance of taxation"
    )


def simulation_insight(amount, target, funding, voucher, result):
    if LANG == "ko":
        voucher_txt = "주거 바우처를 포함한" if voucher else "주거 바우처를 포함하지 않은"
        risk = {
            "tax": "증세 방식은 재정 지속가능성은 비교적 안정적이지만 조세 저항이 커질 수 있습니다",
            "debt": "국채 방식은 단기 확장 효과는 크지만 장기 재정 부담과 세대 간 부담 논쟁이 커질 수 있습니다",
            "merge": "기존 복지 통합 방식은 비용을 줄일 수 있지만 기존 취약계층 지원이 약화될 위험이 있습니다",
        }[result["funding_code"]]
        return (
            f"현재 시나리오는 월 {amount}만원 기본소득, 지급 대상은 {target}, 재원 조달은 {funding}, {voucher_txt} 설계입니다<br><br>"
            f"모델상 청년실업률은 현재 대비 약 {result['unemp_change']:.2f}%p 변화하고, 청년 주거부담률은 약 {result['housing_burden']:.1f}% 수준으로 완화되는 것으로 나타납니다 "
            f"다만 연간 재정 소요가 약 {result['annual_cost']:.1f}조원으로 추정되기 때문에 정책 효과만큼 재원 설계도 중요한 변수입니다<br><br>"
            f"{risk}<br><br>따라서 이 조건은 단순 현금 지급만으로 보기보다 청년 주거 안정, 고용서비스, 직업훈련, 지역 소비 정책을 묶은 패키지로 설계할 때 설득력이 커집니다"
        )

    voucher_txt = "with a housing voucher" if voucher else "without a housing voucher"
    risk = {
        "tax": "A tax-based model is relatively stable in fiscal terms, but it may face stronger taxpayer resistance",
        "debt": "A debt-based model can create a stronger short-term stimulus, but it increases long-term fiscal and intergenerational burden",
        "merge": "A welfare-integration model reduces headline costs, but it may weaken support for already vulnerable groups",
    }[result["funding_code"]]
    return (
        f"This scenario assumes a monthly basic income of KRW {amount * 10000:,}, targeted at {target}, funded through {funding}, {voucher_txt}<br><br>"
        f"The model estimates a youth unemployment change of about {result['unemp_change']:.2f} percentage points and a youth housing burden rate of about {result['housing_burden']:.1f}% "
        f"However, the estimated annual fiscal cost is about KRW {result['annual_cost']:.1f} trillion, meaning the funding design matters as much as the welfare effect<br><br>"
        f"{risk}<br><br>Overall, this scenario becomes more persuasive when basic income is combined with housing support, employment services, job training, and local consumption policy"
    )


# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.markdown("### 📌 Project")
st.sidebar.info(T["project_note"])

st.sidebar.markdown(f"### 👥 {T['created_by']}")
st.sidebar.markdown(
    """
    <div class="creator-card">
    30307 김단아<br>
    30309 김민정<br>
    30317 어하은<br>
    30324 정서희
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown("### ⚠️ Note")
st.sidebar.caption(T["data_warning"])


# =========================================================
# HEADER
# =========================================================
st.markdown(f'<div class="main-title">{T["title"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sub-title">{T["subtitle"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="question-box">💡 {T["question"]}</div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs([T["overview"], T["welfare"], T["business"], T["simulation"], T["policy"]])


# =========================================================
# TAB 1 OVERVIEW
# =========================================================
with tab1:
    selected_year = st.selectbox(T["year_select"], years, index=len(years) - 1)
    row = main_df.loc[main_df["year"] == selected_year].iloc[0]

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        card(T["youth_unemp"], f"{row['youth_unemployment']:.1f}%", "15~29세 청년 지표" if LANG == "ko" else "15–29 youth indicator", "#4F8CFF")
    with c2:
        card(T["housing_burden"], f"{row['housing_burden']:.1f}%", "주거비 / 소득 기준" if LANG == "ko" else "Housing cost / income", "#FFB020")
    with c3:
        card(T["ubi_cases"], f"{int(row['ubi_case_count'])}", "주요 실험·논의 사례" if LANG == "ko" else "Selected global cases", "#32D583")
    with c4:
        card(T["welfare_spend"], f"{row['welfare_spending']:.1f}%", "GDP 대비 공공사회복지지출" if LANG == "ko" else "Public social spending / GDP", "#A78BFA")

    section("분석 구조" if LANG == "ko" else "Dashboard logic")
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown(
            f"""
            <div class="policy-card">
            <b>① {'문제 진단' if LANG == 'ko' else 'Problem'}</b><br><br>
            {'청년 고용 불안과 주거비 부담이 동시에 커지는 구조를 확인합니다' if LANG == 'ko' else 'The dashboard first identifies the combined pressure of youth unemployment and housing costs'}
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_b:
        st.markdown(
            f"""
            <div class="policy-card" style="border-left-color:#FFB020;">
            <b>② {'정책 도구' if LANG == 'ko' else 'Policy tool'}</b><br><br>
            {'기본소득을 복지정책이자 소비·재정 정책으로 동시에 분석합니다' if LANG == 'ko' else 'Basic income is analysed as both welfare policy and economic policy'}
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_c:
        st.markdown(
            f"""
            <div class="policy-card" style="border-left-color:#32D583;">
            <b>③ {'정책 시뮬레이션' if LANG == 'ko' else 'Simulation'}</b><br><br>
            {'지급액, 대상, 재원, 주거 바우처 여부를 바꿔 정책 효과를 비교합니다' if LANG == 'ko' else 'Users compare effects by changing payment amount, target group, funding method, and housing voucher design'}
            </div>
            """,
            unsafe_allow_html=True,
        )
    caption(T["source_note"])


# =========================================================
# TAB 2 SOCIAL WELFARE
# =========================================================
with tab2:
    section("한국 청년 실업률 추이" if LANG == "ko" else "Korea youth unemployment trend")
    fig = px.line(
        main_df,
        x="year",
        y="youth_unemployment",
        markers=True,
        labels={"year": "연도" if LANG == "ko" else "Year", "youth_unemployment": "청년실업률 (%)" if LANG == "ko" else "Youth unemployment rate (%)"},
    )
    fig.update_traces(line={"width": 4, "color": "#4F8CFF"}, marker={"size": 9})
    apply_plotly_style(fig, height=390, x_title="연도" if LANG == "ko" else "Year", y_title="%")
    st.plotly_chart(fig, use_container_width=True)
    caption()

    col1, col2 = st.columns(2)

    with col1:
        section("OECD 주요국 청년실업률 비교" if LANG == "ko" else "OECD youth unemployment comparison")
        country_col = "country_ko" if LANG == "ko" else "country_en"
        fig2 = px.bar(
            oecd_df,
            x=country_col,
            y="youth_unemployment",
            labels={country_col: "국가" if LANG == "ko" else "Country", "youth_unemployment": "청년실업률 (%)" if LANG == "ko" else "Youth unemployment rate (%)"},
        )
        fig2.update_traces(marker_color=["#4F8CFF", "#32D583", "#A78BFA", "#FFB020", "#F97066", "#94A3B8"])
        apply_plotly_style(fig2, height=360, x_title="국가" if LANG == "ko" else "Country", y_title="%")
        st.plotly_chart(fig2, use_container_width=True)
        caption("자료: OECD 청년실업률 지표, 국가별 기준 차이 있음" if LANG == "ko" else "Source: OECD youth unemployment indicator; definitions may differ by country")

    with col2:
        section("청년 주거 부담률 추이" if LANG == "ko" else "Youth housing burden trend")
        fig3 = px.area(
            main_df,
            x="year",
            y="housing_burden",
            labels={"year": "연도" if LANG == "ko" else "Year", "housing_burden": "주거부담률 (%)" if LANG == "ko" else "Housing burden rate (%)"},
        )
        fig3.update_traces(line={"width": 3, "color": "#FFB020"}, fillcolor="rgba(255,176,32,0.28)")
        apply_plotly_style(fig3, height=360, x_title="연도" if LANG == "ko" else "Year", y_title="%")
        st.plotly_chart(fig3, use_container_width=True)
        caption("자료: 청년 주거비 부담 논의를 바탕으로 한 교육용 재구성" if LANG == "ko" else "Source: Educational reconstruction based on youth housing affordability discussions")

    section(T["case_title"])
    case_cols = st.columns(3)
    for idx, item in enumerate(case_cards[LANG]):
        with case_cols[idx]:
            st.markdown(
                f"""
                <div class="card">
                    <div style="color:#32D583; font-weight:900; margin-bottom:8px;">{item['tag']}</div>
                    <div style="font-size:1.1rem; font-weight:950; margin-bottom:10px; color:#FFFFFF;">{item['title']}</div>
                    <div style="color:#E2E8F0; line-height:1.58; font-size:0.92rem; font-weight:650;">{item['body']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    if st.button(T["ai_welfare"], key="ai_welfare"):
        insight_stream(simple_ai_text("welfare"))


# =========================================================
# TAB 3 BUSINESS ECONOMICS
# =========================================================
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        section("기본소득 재원 조달 방식별 부담 비교" if LANG == "ko" else "Fiscal burden by funding method")
        method_col = "method_ko" if LANG == "ko" else "method_en"
        fig4 = px.bar(
            funding_df,
            x=method_col,
            y=["fiscal_burden", "political_risk"],
            barmode="group",
            labels={method_col: "재원 조달 방식" if LANG == "ko" else "Funding method", "value": "부담 지수" if LANG == "ko" else "Burden index", "variable": "항목" if LANG == "ko" else "Metric"},
        )
        apply_plotly_style(fig4, height=400, x_title="재원 조달 방식" if LANG == "ko" else "Funding method", y_title="Index")
        st.plotly_chart(fig4, use_container_width=True)
        caption()

    with col2:
        section("기본소득 지급 시 소비 진작 효과" if LANG == "ko" else "Consumption stimulus simulation")
        fig5 = go.Figure()
        labels = ["낮은 지급액", "중간 지급액", "높은 지급액"] if LANG == "ko" else ["Low", "Medium", "High"]
        for col, name, color in zip(["low", "medium", "high"], labels, ["#4F8CFF", "#32D583", "#FFB020"]):
            fig5.add_trace(go.Scatter(x=consumption_df["year"], y=consumption_df[col], mode="lines+markers", name=name, line={"width": 3, "color": color}))
        apply_plotly_style(fig5, height=400, x_title="연도" if LANG == "ko" else "Year", y_title="GDP 대비 %" if LANG == "ko" else "% of GDP")
        st.plotly_chart(fig5, use_container_width=True)
        caption("자료: 가상 소비승수 시나리오" if LANG == "ko" else "Source: Hypothetical consumption multiplier scenario")

    section("업종별 청년 고용률 vs 평균임금" if LANG == "ko" else "Youth employment rate vs average wage by sector")
    sector_col = "sector_ko" if LANG == "ko" else "sector_en"
    fig6 = px.scatter(
        sector_df,
        x="youth_employment_rate",
        y="avg_wage",
        size="stability",
        color=sector_col,
        labels={
            "youth_employment_rate": "청년 고용률 (%)" if LANG == "ko" else "Youth employment rate (%)",
            "avg_wage": "평균임금 (만원)" if LANG == "ko" else "Average wage (KRW 10,000)",
            sector_col: "업종" if LANG == "ko" else "Sector",
        },
    )
    apply_plotly_style(fig6, height=440, x_title="청년 고용률 (%)" if LANG == "ko" else "Youth employment rate (%)", y_title="평균임금 (만원)" if LANG == "ko" else "Average wage")
    st.plotly_chart(fig6, use_container_width=True)
    caption("자료: 업종별 고용·임금 구조를 단순화한 교육용 데이터" if LANG == "ko" else "Source: Simplified educational dataset on sectoral employment and wages")

    if st.button(T["ai_business"], key="ai_business"):
        insight_stream(simple_ai_text("business"))


# =========================================================
# TAB 4 SIMULATION
# =========================================================
with tab4:
    st.markdown(f'<div class="scenario-banner">⚠️ {T["simulation_note"]}</div>', unsafe_allow_html=True)
    input_col, output_col = st.columns([0.95, 1.45])

    with input_col:
        section("조정 변수" if LANG == "ko" else "Policy controls")
        amount = st.slider(T["monthly_amount"], min_value=0, max_value=100, value=50, step=5, format="%d만원" if LANG == "ko" else "%d")
        target = st.radio(T["target"], [T["youth_only"], T["all_people"]], index=0)
        funding = st.radio(T["funding"], [T["tax"], T["debt"], T["merge"]], index=0)
        voucher = st.toggle(T["voucher"], value=True)

        result = scenario_calculation(amount, target, funding, voucher)
        st.session_state["last_amount"] = amount
        st.session_state["last_target"] = target
        st.session_state["last_funding"] = funding
        st.session_state["last_voucher"] = voucher
        st.session_state["last_result"] = result

        st.markdown("---")
        st.metric("연간 재정 소요 추정" if LANG == "ko" else "Estimated annual fiscal cost", f"{result['annual_cost']:.1f}조원" if LANG == "ko" else f"KRW {result['annual_cost']:.1f} tn")
        st.metric("소비 진작 효과" if LANG == "ko" else "Consumption stimulus", f"GDP 대비 {result['gdp_effect']:.2f}%" if LANG == "ko" else f"{result['gdp_effect']:.2f}% of GDP")

    with output_col:
        section("실시간 결과 차트" if LANG == "ko" else "Live simulation outputs")
        sim_years = [2024, 2025, 2026, 2027, 2028]
        unemp_path = np.linspace(5.9, result["projected_unemp"], len(sim_years))
        housing_path = [27.2, result["housing_burden"]]

        fig7 = go.Figure()
        fig7.add_trace(go.Scatter(x=sim_years, y=unemp_path, mode="lines+markers", name=T["youth_unemp"], line={"width": 4, "color": "#4F8CFF"}, marker={"size": 9}))
        fig7.add_hline(y=5.9, line_dash="dash", line_color="#CBD5E1", annotation_text="현재 기준" if LANG == "ko" else "Current baseline")
        apply_plotly_style(fig7, height=330, title="청년 실업률 변화 예측" if LANG == "ko" else "Projected youth unemployment change", x_title="연도" if LANG == "ko" else "Year", y_title="%")
        st.plotly_chart(fig7, use_container_width=True)

        col_a, col_b = st.columns(2)

        with col_a:
            fig8 = go.Figure()
            fig8.add_trace(go.Bar(x=["현재", "시뮬레이션"] if LANG == "ko" else ["Current", "Simulation"], y=housing_path, marker_color=["#94A3B8", "#FFB020"]))
            apply_plotly_style(fig8, height=330, title="청년 주거 부담률 변화" if LANG == "ko" else "Youth housing burden change", y_title="%")
            st.plotly_chart(fig8, use_container_width=True)

        with col_b:
            fig9 = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=result["annual_cost"],
                    number={"suffix": "조원" if LANG == "ko" else " tn", "font": {"color": "#F8FAFC", "size": 40}},
                    title={"text": "연간 재정 소요" if LANG == "ko" else "Annual fiscal cost", "font": {"color": "#FFFFFF", "size": 20}},
                    gauge={
                        "axis": {"range": [0, 360], "tickcolor": "#F8FAFC", "tickfont": {"color": "#F8FAFC"}},
                        "bar": {"color": "#A78BFA"},
                        "steps": [
                            {"range": [0, 80], "color": "rgba(50,213,131,0.26)"},
                            {"range": [80, 180], "color": "rgba(255,176,32,0.26)"},
                            {"range": [180, 360], "color": "rgba(249,112,102,0.26)"},
                        ],
                    },
                )
            )
            fig9.update_layout(template="plotly_dark", height=330, paper_bgcolor="#0F1117", plot_bgcolor="#0F1117", font={"color": "#F8FAFC"}, margin={"l": 30, "r": 30, "t": 58, "b": 25})
            st.plotly_chart(fig9, use_container_width=True)

        gdp_path = np.linspace(0, result["gdp_effect"], len(sim_years))
        fig10 = go.Figure()
        fig10.add_trace(go.Scatter(x=sim_years, y=gdp_path, fill="tozeroy", mode="lines", name="GDP effect", line={"width": 4, "color": "#32D583"}, fillcolor="rgba(50,213,131,0.28)"))
        apply_plotly_style(fig10, height=310, title="소비 진작 효과 GDP 대비 %" if LANG == "ko" else "Consumption stimulus as % of GDP", x_title="연도" if LANG == "ko" else "Year", y_title="%")
        st.plotly_chart(fig10, use_container_width=True)

        radar_categories = ["소득 안정", "주거 안정", "고용 완화", "재정 안정", "정책 실행성"] if LANG == "ko" else ["Income security", "Housing stability", "Employment relief", "Fiscal stability", "Feasibility"]
        radar_values = [
            result["satisfaction"],
            100 - result["housing_burden"] * 2.1,
            100 - result["projected_unemp"] * 9.0,
            result["fiscal_stability"],
            result["feasibility"],
        ]
        radar_values = [max(0, min(100, value)) for value in radar_values]

        fig11 = go.Figure()
        fig11.add_trace(
            go.Scatterpolar(
                r=radar_values + [radar_values[0]],
                theta=radar_categories + [radar_categories[0]],
                fill="toself",
                name="지수" if LANG == "ko" else "Index",
                line={"color": "#A78BFA", "width": 3},
                fillcolor="rgba(167,139,250,0.28)",
            )
        )
        fig11.update_layout(
            template="plotly_dark",
            height=410,
            title="복지 만족도 지수 레이더 차트" if LANG == "ko" else "Welfare satisfaction radar index",
            font={"color": "#F8FAFC", "size": 14},
            title_font={"color": "#FFFFFF", "size": 20},
            polar={
                "bgcolor": "#0F1117",
                "radialaxis": {"visible": True, "range": [0, 100], "tickfont": {"color": "#CBD5E1"}, "gridcolor": "rgba(226,232,240,0.28)"},
                "angularaxis": {"tickfont": {"color": "#F8FAFC", "size": 13}, "gridcolor": "rgba(226,232,240,0.20)"},
            },
            paper_bgcolor="#0F1117",
            plot_bgcolor="#0F1117",
            margin={"l": 40, "r": 40, "t": 70, "b": 40},
        )
        st.plotly_chart(fig11, use_container_width=True)
        caption("자료: 사용자가 조정한 가상 정책 시나리오 기반" if LANG == "ko" else "Source: User-controlled hypothetical policy scenario")

    if st.button(T["ai_sim"], key="ai_simulation"):
        with st.spinner("분석 중..." if LANG == "ko" else "Analysing..."):
            time.sleep(0.4)
        insight_stream(simulation_insight(amount, target, funding, voucher, result))


# =========================================================
# TAB 5 POLICY RECOMMENDATIONS
# =========================================================
with tab5:
    default_result = scenario_calculation(50, T["youth_only"], T["tax"], True)
    result = st.session_state.get("last_result", default_result)
    amount = st.session_state.get("last_amount", 50)
    target = st.session_state.get("last_target", T["youth_only"])
    funding = st.session_state.get("last_funding", T["tax"])
    voucher = st.session_state.get("last_voucher", True)

    section(T["last_scenario"])

    s1, s2, s3, s4 = st.columns(4)
    s1.metric(T["monthly_amount"], f"{amount}만원" if LANG == "ko" else f"KRW {amount * 10000:,}")
    s2.metric(T["target"], target)
    s3.metric(T["funding"], funding)
    s4.metric(T["voucher"], "ON" if voucher else "OFF")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div class="policy-card">
            <h3>{T['short_term']}</h3>
            <b>{'부분 지급 + 주거 바우처 실험' if LANG == 'ko' else 'Partial payment + housing voucher pilot'}</b><br><br>
            {'청년층 일부를 대상으로 기본소득과 주거 바우처를 결합해 정책 효과를 먼저 측정합니다 고용률보다 생활 안정, 구직 지속성, 월세 부담 변화를 우선 지표로 삼는 것이 적절합니다' if LANG == 'ko' else 'Begin with a limited youth-focused pilot combining basic income and housing vouchers The first indicators should be living stability, job-search continuity, and rent burden rather than employment rate alone'}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f"""
            <div class="policy-card" style="border-left-color:#FFB020;">
            <h3>{T['mid_term']}</h3>
            <b>{'고용서비스·지역경제 연동' if LANG == 'ko' else 'Link with employment services and local economy'}</b><br><br>
            {'현금 지급만으로 끝내지 말고 직업훈련, 상담, 지역화폐형 소비 효과를 함께 측정합니다 이 단계에서는 재원 조달 방식별 정치적 수용성과 비용 대비 효과를 비교해야 합니다' if LANG == 'ko' else 'Do not stop at cash transfers Connect the program with job training, counselling, and local consumption measurement At this stage, compare political acceptance and cost-effectiveness by funding method'}
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            f"""
            <div class="policy-card" style="border-left-color:#32D583;">
            <h3>{T['long_term']}</h3>
            <b>{'선별 확대 또는 조건 없는 보장소득 모델' if LANG == 'ko' else 'Selective expansion or guaranteed income model'}</b><br><br>
            {'전 국민 보편 지급은 재정 부담이 크기 때문에 실험 결과를 바탕으로 청년, 저소득층, 주거 취약층 중심의 단계적 확대가 더 현실적입니다 장기적으로는 기존 복지와 중복되지 않게 설계해야 합니다' if LANG == 'ko' else 'Universal payment creates heavy fiscal pressure, so gradual expansion focused on youth, low-income groups, and housing-vulnerable groups is more realistic Long-term design should avoid inefficient overlap with existing welfare programs'}
            </div>
            """,
            unsafe_allow_html=True,
        )

    section("국제 비교 정책 테이블" if LANG == "ko" else "International policy comparison table")

    if LANG == "ko":
        policy_table = pd.DataFrame(
            {
                "국가": ["핀란드", "독일", "한국"],
                "정책 초점": ["실업자 기본소득 실험", "주거·사회보장 중심 복지", "청년소득·주거지원 혼합"],
                "강점": ["삶의 만족도와 정신적 안정 분석", "기존 복지체계와의 연결성", "청년층 맞춤형 정책 실험 가능"],
                "한계": ["고용 증가 효과는 제한적", "전면 기본소득보다는 복지국가 모델에 가까움", "재원과 정치적 합의가 핵심 변수"],
            }
        )
    else:
        policy_table = pd.DataFrame(
            {
                "Country": ["Finland", "Germany", "Korea"],
                "Policy focus": ["Basic income experiment for unemployed people", "Housing and social security welfare model", "Youth income and housing support mix"],
                "Strength": ["Useful for analysing life satisfaction and psychological stability", "Strong connection with existing welfare institutions", "High potential for youth-targeted policy experiments"],
                "Limitation": ["Employment effect was limited", "Closer to a welfare-state model than full UBI", "Funding and political consensus are key variables"],
            }
        )

    st.dataframe(policy_table, use_container_width=True, hide_index=True)

    if st.button(T["ai_policy"], key="ai_policy"):
        insight_stream(simple_ai_text("policy"))


# =========================================================
# FOOTER
# =========================================================
st.markdown(
    f"""
    <div class="footer">
    <b>Sources / 출처</b><br>
    KOSIS Korean Statistical Information Service · OECD Data Youth Unemployment Rate · OECD Social Expenditure Database SOCX · Bank of Korea macroeconomic context · Public reports on Finland, Gyeonggi, and Canada basic income discussions<br><br>
    <b>Methodological note / 방법론 메모</b><br>
    {T['footer']}<br>
    Youth definitions differ by source Korean labour statistics often use ages 15–29, while OECD youth unemployment indicators commonly use ages 15–24
    </div>
    """,
    unsafe_allow_html=True,
)
