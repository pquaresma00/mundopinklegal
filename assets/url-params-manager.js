/**
 * URL Parameters Manager
 * Gerencia parâmetros de URL usando pushState para preservar em cada página
 */

(function() {
    'use strict';

    // Armazena os parâmetros iniciais da URL
    const initialParams = new URLSearchParams(window.location.search);
    const paramsToPreserve = [
        'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
        'fbclid', 'gclid', 'msclkid', 'ttclid', 'click_id'
    ];

    // Função para extrair parâmetros relevantes
    function extractRelevantParams(search) {
        const params = new URLSearchParams(search);
        const relevant = new URLSearchParams();
        
        paramsToPreserve.forEach(key => {
            const value = params.get(key);
            if (value) {
                relevant.set(key, value);
            }
        });
        
        return relevant;
    }

    // Função para mesclar parâmetros preservados com novos parâmetros
    function mergeParams(newParams, preserveParams) {
        const merged = new URLSearchParams(newParams);
        
        // Adiciona parâmetros preservados que não estão nos novos
        preserveParams.forEach((value, key) => {
            if (!merged.has(key)) {
                merged.set(key, value);
            }
        });
        
        return merged;
    }

    // Intercepta navegação via pushState/replaceState
    const originalPushState = history.pushState;
    const originalReplaceState = history.replaceState;

    history.pushState = function(state, title, url) {
        if (url) {
            const urlObj = new URL(url, window.location.origin);
            const currentParams = extractRelevantParams(window.location.search);
            const newParams = extractRelevantParams(urlObj.search);
            const mergedParams = mergeParams(newParams, currentParams);
            
            // Reconstrói a URL com parâmetros mesclados
            urlObj.search = mergedParams.toString();
            url = urlObj.pathname + (mergedParams.toString() ? '?' + mergedParams.toString() : '') + urlObj.hash;
        }
        
        return originalPushState.call(history, state, title, url);
    };

    history.replaceState = function(state, title, url) {
        if (url) {
            const urlObj = new URL(url, window.location.origin);
            const currentParams = extractRelevantParams(window.location.search);
            const newParams = extractRelevantParams(urlObj.search);
            const mergedParams = mergeParams(newParams, currentParams);
            
            // Reconstrói a URL com parâmetros mesclados
            urlObj.search = mergedParams.toString();
            url = urlObj.pathname + (mergedParams.toString() ? '?' + mergedParams.toString() : '') + urlObj.hash;
        }
        
        return originalReplaceState.call(history, state, title, url);
    };

    // Intercepta cliques em links
    document.addEventListener('click', function(e) {
        const link = e.target.closest('a');
        if (!link || link.target === '_blank' || link.hasAttribute('download')) {
            return;
        }

        const href = link.getAttribute('href');
        if (!href || href.startsWith('#') || href.startsWith('javascript:') || href.startsWith('mailto:') || href.startsWith('tel:')) {
            return;
        }

        try {
            const url = new URL(href, window.location.origin);
            
            // Se for mesma origem, preserva parâmetros
            if (url.origin === window.location.origin) {
                const currentParams = extractRelevantParams(window.location.search);
                const linkParams = extractRelevantParams(url.search);
                const mergedParams = mergeParams(linkParams, currentParams);
                
                if (mergedParams.toString()) {
                    url.search = mergedParams.toString();
                    link.href = url.pathname + '?' + mergedParams.toString() + (url.hash || '');
                }
            }
        } catch (err) {
            console.warn('Erro ao processar URL:', err);
        }
    }, true);

    // Preserva parâmetros ao carregar a página
    if (initialParams.toString()) {
        const relevantParams = extractRelevantParams(initialParams);
        if (relevantParams.toString()) {
            const currentUrl = new URL(window.location.href);
            const currentRelevant = extractRelevantParams(currentUrl.search);
            
            // Se houver parâmetros relevantes, garante que estão na URL
            if (relevantParams.toString() !== currentRelevant.toString()) {
                const merged = mergeParams(currentRelevant, relevantParams);
                if (merged.toString()) {
                    currentUrl.search = merged.toString();
                    history.replaceState(null, '', currentUrl.toString());
                }
            }
        }
    }

    // Função global para obter parâmetros preservados
    window.getPreservedParams = function() {
        return extractRelevantParams(window.location.search);
    };

    // Função global para adicionar parâmetros preservados a uma URL
    window.addPreservedParams = function(url) {
        try {
            const urlObj = new URL(url, window.location.origin);
            const currentParams = extractRelevantParams(window.location.search);
            const urlParams = extractRelevantParams(urlObj.search);
            const merged = mergeParams(urlParams, currentParams);
            
            if (merged.toString()) {
                urlObj.search = merged.toString();
                return urlObj.pathname + '?' + merged.toString() + (urlObj.hash || '');
            }
            return urlObj.pathname + (urlObj.hash || '');
        } catch (err) {
            console.warn('Erro ao adicionar parâmetros:', err);
            return url;
        }
    };

    console.log('[URL Params Manager] Inicializado - Parâmetros preservados:', Array.from(extractRelevantParams(window.location.search).keys()));
})();
