// src/lib/utils/api.ts
import { accessToken } from '$lib/stores/authStore';
import { goto } from '$app/navigation';

interface ApiOptions extends RequestInit {
    auth?: boolean; // whether to attach token (default true)
    contentType?: 'json' | 'form' | 'none'; // request body type
    body?: any; // payload (object, FormData, string, etc.)
}

export async function apiFetch(endpoint: string, options: ApiOptions = {}) {
    const { auth = true, contentType = 'json' } = options;
    let token = localStorage.getItem('access_token');

    // Handle auth check
    if (auth && !token) {
        accessToken.set(null);
        goto('/login');
        throw new Error('Not authenticated');
    }

    let headers: Record<string, string> = { ...(options.headers as Record<string, string>) };

    // Set Content-Type only if needed
    if (contentType === 'json') {
        headers['Content-Type'] = 'application/json';
    } else if (contentType === 'form') {
        headers['Content-Type'] = 'application/x-www-form-urlencoded';
    }

    // Attach auth header if required
    if (auth && token) {
        headers['Authorization'] = `Bearer ${token}`;
    }

    // Encode body depending on content type
    let body = options.body;
    if (contentType === 'json' && body && typeof body !== 'string') {
        body = JSON.stringify(body);
    } else if (contentType === 'form' && body && !(body instanceof URLSearchParams)) {
        const formData = new URLSearchParams();
        for (const key in body) {
            formData.append(key, body[key]);
        }
        body = formData.toString();
    }

    const response = await fetch(`http://localhost:8000${endpoint}`, {
        ...options,
        headers,
        body,
    });

    if (response.status === 401) {
        localStorage.removeItem('access_token');
        accessToken.set(null);
        goto('/login');
        throw new Error('Authentication failed');
    }

    if (!response.ok) {
        let errorMsg = 'Unknown error';
        try {
            const data = await response.json();
            errorMsg = data.detail || errorMsg;
        } catch {}
        throw new Error(errorMsg);
    }

    try {
        return await response.json(); // Most endpoints return JSON
    } catch {
        return null; // Handle empty response (e.g., DELETE)
    }
}
