from graph_config import CONSENT, TRACKING, POINT_COLOR, LINE_COLORS, RIGHT_SYM, LEFT_SYM, X_PAD, DOMAIN_PAD, CODOMAIN_PAD, TPDOMAINS_PATH, OUTPUT_PATH
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import pandas as pd

def build_domain(points, pad):
    
    interval = 1 - pad * 2
    space = interval / max((len(points) - 1), 1)
    
    domain = dict()
    
    for i, point in enumerate(points):
        domain[point] = round(1 - pad - (space * i), 4)
        
    return domain

def prepare_df(tp_domains):
    
    tp_domains = tp_domains.loc[tp_domains['Tracking'] == TRACKING]
    tp_domains = tp_domains[['LLM', 'Organization', 'CONSENT']]
    tp_domains = tp_domains.drop_duplicates()
    
    tp_domains = tp_domains.loc[tp_domains['CONSENT'] != CONSENT['1']]
    tp_domains['CONSENT'] = tp_domains['CONSENT'].replace({CONSENT['0']: 'solid', CONSENT['3']: 'solid', CONSENT['2']: 'dashed'})
    
    tp_domains = tp_domains.assign(priority=(tp_domains['CONSENT'] != 'dashed')).sort_values('priority')
    tp_domains = tp_domains.drop_duplicates(subset=['LLM', 'Organization'])
    tp_domains = tp_domains.drop(columns='priority')
    
    connections = list(tp_domains.itertuples(index=False, name=None))
    
    llms = tp_domains[['LLM']]['LLM'].unique().tolist()
    llms.sort()
    
    tps = tp_domains[['Organization']]['Organization'].unique().tolist()
    tps.sort()
    
    return connections, build_domain(llms, DOMAIN_PAD), build_domain(tps, CODOMAIN_PAD)

def draw_curve(axis, x0, y0, x1, y1, linestyle, color):
    
    control1 = (x0 + (x1 - x0) * 0.5, y0)
    control2 = (x0 + (x1 - x0) * 0.5, y1)

    path = Path(
        [(x0, y0), control1, control2, (x1, y1)],
        [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4],
    )

    patch = patches.PathPatch(
        path, facecolor="none", edgecolor=color,
        linestyle=linestyle, linewidth=2, alpha=0.8, zorder=1,
    )

    axis.add_patch(patch)
    
def draw_point(axis, x, y, symbol, pad, label, alignment):
    
    axis.plot(x, y, symbol, color=POINT_COLOR, markersize=9, zorder=3)
    axis.text(x + pad, y, label, color=POINT_COLOR, fontsize=11, ha=alignment, va='center')

def draw_graph(path_domains):
    
    tp_domains = pd.read_csv(path_domains)
    connections, llms, tps = prepare_df(tp_domains)
    
    figure, axis = plt.subplots(figsize=(7, 6))
    
    for llm, tp, style in connections:
        
        draw_curve(axis, 0, llms[llm], 1, tps[tp], style, LINE_COLORS[style])
        
    for llm, y in llms.items():
        
        draw_point(axis, 0, y, LEFT_SYM, -X_PAD, llm, 'right')
        
    for tp, y in tps.items():
        
        draw_point(axis, 1, y, RIGHT_SYM, X_PAD, tp, 'left')
        
    axis.set_xlim(-0.04, 1.04)
    axis.set_ylim(0.05, 0.95)
    axis.axis("off")
    
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH, dpi=150, bbox_inches="tight")
    
if __name__ == "__main__":
    draw_graph(TPDOMAINS_PATH)