import os
import re

BASE_PATH = r"C:\Users\filip\.gemini\antigravity\scratch\inventario-portage"
FILES = ['index.html', 'spm.html', 'resumo.html', 'portage.html', 'rotina.html', 'login.html']

def get_bottom_nav(active_page):
    def a(page): return 'text-indigo-600' if page == active_page else 'text-slate-500'
    
    # SVG Definitions
    svg_rotina = '<svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>'
    svg_diario = '<svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>'
    svg_resumo = '<svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"></path></svg>'
    svg_portage = '<svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"></path></svg>'
    svg_spm = '<svg class="w-6 h-6 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 4a2 2 0 114 0v1a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-1a2 2 0 100 4h1a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-1a2 2 0 10-4 0v1a1 1 0 01-1 1H7a1 1 0 01-1-1v-3a1 1 0 00-1-1H4a2 2 0 110-4h1a1 1 0 001-1V7a1 1 0 011-1h3a1 1 0 001-1V4z"></path></svg>'

    # Order: Rotina -> Diário -> Resumo -> Portage -> SPM
    # Max of 5 buttons is okay for mobile PWA. Let's make them slightly smaller horizontally by adjusting padding.
    return f"""
    <!-- Bottom Navigation Bar (PWA) -->
    <nav class="no-print fixed bottom-0 w-full bg-white border-t border-slate-200 shadow-[0_-4px_10px_rgba(0,0,0,0.05)] z-[100] pb-safe" style="padding-bottom: env(safe-area-inset-bottom);">
        <div class="max-w-md mx-auto flex justify-between items-center h-16 px-1">
            <a href="rotina.html" class="flex flex-col items-center justify-center w-full h-full hover:bg-slate-50 transition-colors {a('rotina')}">
                {svg_rotina}
                <span class="text-[9px] font-bold">Rotina</span>
            </a>
            <a href="index.html" class="flex flex-col items-center justify-center w-full h-full hover:bg-slate-50 transition-colors {a('index')}">
                {svg_diario}
                <span class="text-[9px] font-bold">Diário</span>
            </a>
            <a href="resumo.html" class="flex flex-col items-center justify-center w-full h-full hover:bg-slate-50 transition-colors {a('resumo')}">
                {svg_resumo}
                <span class="text-[9px] font-bold">Resumo</span>
            </a>
            <a href="portage.html" class="flex flex-col items-center justify-center w-full h-full hover:bg-slate-50 transition-colors {a('portage')}">
                {svg_portage}
                <span class="text-[9px] font-bold">Portage</span>
            </a>
            <a href="spm.html" class="flex flex-col items-center justify-center w-full h-full hover:bg-slate-50 transition-colors {a('spm')}">
                {svg_spm}
                <span class="text-[9px] font-bold">SPM</span>
            </a>
        </div>
    </nav>
"""

# Replace navigation in all files
for f in FILES:
    filepath = os.path.join(BASE_PATH, f)
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    active_page = f.split('.')[0]
    
    nav_regex = re.compile(r'<!-- Bottom Navigation Bar \(PWA\) -->\s*<nav.*?</nav>', re.DOTALL)
    content = nav_regex.sub('', content)

    # Exclude login.html from getting the nav
    if f != 'login.html':
        bot = get_bottom_nav(active_page)
        content = content.replace('</body>', f'{bot}\n</body>')

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

print("Updated navigation bar in all files.")
