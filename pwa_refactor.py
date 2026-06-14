import os
import re

FILES = ['index.html', 'spm.html', 'resumo.html', 'diario.html', 'login.html']
BASE_PATH = r"C:\Users\filip\.gemini\antigravity\scratch\inventario-portage"

def get_bottom_nav(active_page):
    def a(page): return 'text-indigo-600' if page == active_page else 'text-slate-500'
    return f"""
    <!-- Bottom Navigation Bar (PWA) -->
    <nav class="no-print fixed bottom-0 w-full bg-white border-t border-slate-200 shadow-[0_-4px_10px_rgba(0,0,0,0.05)] z-[100] pb-safe" style="padding-bottom: env(safe-area-inset-bottom);">
        <div class="max-w-md mx-auto flex justify-around items-center h-16 px-2">
            <a href="index.html" class="flex flex-col items-center justify-center w-full h-full hover:bg-slate-50 transition-colors {a('index')}">
                <svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path></svg>
                <span class="text-[10px] font-semibold">Portage</span>
            </a>
            <a href="spm.html" class="flex flex-col items-center justify-center w-full h-full hover:bg-slate-50 transition-colors {a('spm')}">
                <svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 4a2 2 0 114 0v1a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-1a2 2 0 100 4h1a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-1a2 2 0 10-4 0v1a1 1 0 01-1 1H7a1 1 0 01-1-1v-3a1 1 0 00-1-1H4a2 2 0 110-4h1a1 1 0 001-1V7a1 1 0 011-1h3a1 1 0 001-1V4z"></path></svg>
                <span class="text-[10px] font-semibold">SPM</span>
            </a>
            <a href="resumo.html" class="flex flex-col items-center justify-center w-full h-full hover:bg-slate-50 transition-colors {a('resumo')}">
                <svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"></path></svg>
                <span class="text-[10px] font-semibold">Resumo</span>
            </a>
            <a href="diario.html" class="flex flex-col items-center justify-center w-full h-full hover:bg-slate-50 transition-colors {a('diario')}">
                <svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                <span class="text-[10px] font-semibold">Diário</span>
            </a>
        </div>
    </nav>
"""

def get_top_app_bar(title, show_sync=False):
    sync_html = """
                <div id="sync-status" class="flex items-center text-xs font-semibold text-indigo-200 bg-indigo-700/50 px-2 py-1 rounded-full border border-indigo-500/30 shadow-inner">
                    <span class="w-1.5 h-1.5 rounded-full bg-slate-300 mr-1.5 inline-block"></span>
                    <span>Offline</span>
                </div>
""" if show_sync else ""
    return f"""
    <!-- Top App Bar (PWA) -->
    <header class="bg-indigo-600 text-white shadow-md sticky top-0 z-40 no-print" style="padding-top: env(safe-area-inset-top);">
        <div class="max-w-5xl mx-auto px-4 h-14 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center font-black text-white shadow-inner">E</div>
                <h1 class="font-bold text-lg tracking-tight">{title}</h1>
            </div>
            <div class="flex items-center space-x-3">
{sync_html}
                <button onclick="localStorage.removeItem('auth'); window.location.href='login.html';" class="p-2 -mr-2 text-indigo-100 hover:text-white transition-colors" title="Sair">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path></svg>
                </button>
            </div>
        </div>
    </header>
"""

# HTML Meta tags
pwa_meta = """    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#4f46e5">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
"""

for f in FILES:
    filepath = os.path.join(BASE_PATH, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Inject meta tags
    if '<link rel="manifest"' not in content:
        content = content.replace('<title>', pwa_meta + '    <title>')
        
    # Remove old navbar
    navbar_regex = re.compile(r'<!-- Navbar -->\s*<nav.*?</nav>', re.DOTALL)
    content = navbar_regex.sub('', content)

    # 2. Add Top App Bar and Bottom Nav
    if f == 'index.html':
        content = content.replace('<body class="', '<body class="pb-24 ')
        top = get_top_app_bar('Inventário Portage', show_sync=True)
        bot = get_bottom_nav('index')
        content = content.replace('<body class="pb-24 bg-slate-50 text-slate-800 font-sans antialiased">', f'<body class="pb-24 bg-slate-50 text-slate-800 font-sans antialiased">\n{top}')
        content = content.replace('</body>', f'{bot}\n</body>')
        
        # Remove floating bubble
        float_regex = re.compile(r'<div class="no-print fixed bottom-6 right-6.*?</button>\s*</div>', re.DOTALL)
        content = float_regex.sub('', content)

        # Add FAB for Save and end-of-page Actions
        actions_html = """
        <!-- End of Page Actions (PWA) -->
        <div class="mt-8 bg-white p-6 rounded-2xl border border-slate-200 shadow-sm no-print mb-10 flex flex-wrap gap-3 justify-center">
            <button onclick="showHistoryModal()" class="bg-purple-100 hover:bg-purple-200 text-purple-700 px-5 py-3 rounded-xl font-bold transition-all shadow-sm flex items-center gap-2">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> Histórico
            </button>
            <button onclick="showResultsModal()" class="bg-indigo-100 hover:bg-indigo-200 text-indigo-700 px-5 py-3 rounded-xl font-bold transition-all shadow-sm flex items-center gap-2">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg> Resultados
            </button>
            <button onclick="window.print()" class="bg-slate-100 hover:bg-slate-200 text-slate-700 px-5 py-3 rounded-xl font-bold transition-all shadow-sm flex items-center gap-2">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"></path></svg> Imprimir
            </button>
            <button onclick="clearForm()" class="bg-rose-100 hover:bg-rose-200 text-rose-700 px-5 py-3 rounded-xl font-bold transition-all shadow-sm flex items-center gap-2">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg> Limpar
            </button>
        </div>
        
        <!-- FAB Save -->
        <button onclick="forceSaveToSupabase()" class="no-print fixed bottom-20 right-4 sm:right-8 bg-emerald-500 hover:bg-emerald-600 text-white w-14 h-14 rounded-full shadow-2xl z-40 flex items-center justify-center transition-transform active:scale-95" title="Salvar Tudo">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
        </button>
        """
        content = content.replace('<!-- End Content -->', actions_html)
        # remove old sync status updates in script
        content = content.replace("syncStatusCircle.className = 'w-1.5 h-1.5 rounded-full bg-slate-300 mr-1 inline-block';", "syncStatusCircle.className = 'w-1.5 h-1.5 rounded-full bg-slate-300 mr-1.5 inline-block';")
        
    elif f == 'spm.html':
        content = content.replace('<body class="', '<body class="pb-24 ')
        top = get_top_app_bar('Avaliação SPM', show_sync=True)
        bot = get_bottom_nav('spm')
        content = content.replace('<body class="pb-24 bg-slate-50 text-slate-800 font-sans antialiased">', f'<body class="pb-24 bg-slate-50 text-slate-800 font-sans antialiased">\n{top}')
        content = content.replace('</body>', f'{bot}\n</body>')

        # Remove floating bubble
        float_regex = re.compile(r'<div class="no-print fixed bottom-6 right-6.*?</button>\s*</div>', re.DOTALL)
        content = float_regex.sub('', content)

        # Add FAB for Save and end-of-page Actions
        actions_html = """
        <!-- End of Page Actions (PWA) -->
        <div class="mt-8 bg-white p-6 rounded-2xl border border-slate-200 shadow-sm no-print mb-10 flex flex-wrap gap-3 justify-center">
            <button onclick="showHistoryModal()" class="bg-purple-100 hover:bg-purple-200 text-purple-700 px-5 py-3 rounded-xl font-bold transition-all shadow-sm flex items-center gap-2">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> Histórico
            </button>
            <button onclick="showResultsModal()" class="bg-indigo-100 hover:bg-indigo-200 text-indigo-700 px-5 py-3 rounded-xl font-bold transition-all shadow-sm flex items-center gap-2">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg> Resultados Brutos
            </button>
            <button onclick="clearForm()" class="bg-rose-100 hover:bg-rose-200 text-rose-700 px-5 py-3 rounded-xl font-bold transition-all shadow-sm flex items-center gap-2">
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg> Limpar
            </button>
        </div>
        
        <!-- FAB Save -->
        <button onclick="forceSaveToSupabase()" class="no-print fixed bottom-20 right-4 sm:right-8 bg-emerald-500 hover:bg-emerald-600 text-white w-14 h-14 rounded-full shadow-2xl z-40 flex items-center justify-center transition-transform active:scale-95" title="Salvar Tudo">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7"></path></svg>
        </button>
        """
        content = content.replace('<!-- End Content -->', actions_html)
        content = content.replace("syncStatusCircle.className = 'w-1.5 h-1.5 rounded-full bg-slate-300 mr-1 inline-block';", "syncStatusCircle.className = 'w-1.5 h-1.5 rounded-full bg-slate-300 mr-1.5 inline-block';")

    elif f == 'resumo.html':
        content = content.replace('<body class="', '<body class="pb-24 ')
        top = get_top_app_bar('Resumo Clínico')
        bot = get_bottom_nav('resumo')
        content = content.replace('<body class="pb-24 bg-slate-50 text-slate-800 font-sans antialiased">', f'<body class="pb-24 bg-slate-50 text-slate-800 font-sans antialiased">\n{top}')
        content = content.replace('</body>', f'{bot}\n</body>')
        
    elif f == 'diario.html':
        content = content.replace('<body class="', '<body class="pb-24 ')
        top = get_top_app_bar('Diário de Bordo', show_sync=True)
        bot = get_bottom_nav('diario')
        content = content.replace('<body class="pb-24 bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col">', f'<body class="pb-24 bg-slate-50 text-slate-800 font-sans antialiased min-h-screen flex flex-col">\n{top}')
        content = content.replace('</body>', f'{bot}\n</body>')
        # Remove the top block with sync status that used to be inside <main>
        header_regex = re.compile(r'<!-- Header -->.*?</div>\s*</div>', re.DOTALL)
        content = header_regex.sub('', content)

    # write back
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

print("PWA transformation complete.")
