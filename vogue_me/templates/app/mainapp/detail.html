<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>미니멀 테일러드</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: #f8f8f8;
            color: #333;
        }

        .container {
            max-width: 375px;
            margin: 0 auto;
            background: white;
            min-height: 100vh;
        }

        /* Header */
        .header {
            position: relative;
            background: white;
        }

        .product-image {
            width: 100%;
            height: 400px;
            object-fit: cover;
            border-radius: 0 0 20px 20px;
        }

        .nav-buttons {
            position: absolute;
            top: 20px;
            left: 20px;
            right: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .back-btn, .heart-btn {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border: none;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
        }

        .back-btn {
            background: rgba(0, 0, 0, 0.3);
            color: white;
        }

        .heart-btn {
            background: #ff4757;
            color: white;
        }

        .heart-btn.liked {
            background: #0B1220 !important;
        }

        .back-btn:hover {
            background: rgba(0, 0, 0, 0.5);
        }

        .heart-btn:hover {
            background: #ff3838;
        }

        /* Product Info */
        .product-info {
            padding: 24px 20px;
        }

        .product-title {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 12px;
            color: #2d3436;
        }

        .product-description {
            font-size: 14px;
            line-height: 1.5;
            color: #636e72;
            margin-bottom: 16px;
        }

        .read-more {
            color: #0984e3;
            text-decoration: none;
            font-weight: 500;
        }

        .read-more:hover {
            text-decoration: underline;
        }

        /* Audio Player */
        .audio-player {
            background: #f1f2f6;
            border-radius: 12px;
            padding: 16px;
            margin: 20px 0;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .play-btn {
            width: 32px;
            height: 32px;
            border: none;
            background: #2d3436;
            color: white;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .audio-info {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .audio-time {
            font-size: 14px;
            color: #636e72;
        }

        .progress-bar {
            width: 100%;
            height: 4px;
            background: #ddd;
            border-radius: 2px;
            overflow: hidden;
        }

        .progress {
            width: 15%;
            height: 100%;
            background: #2d3436;
            transition: width 0.3s;
        }

        .volume-btn, .more-btn {
            width: 24px;
            height: 24px;
            border: none;
            background: none;
            color: #636e72;
            cursor: pointer;
        }

        /* Environmental Info */
        .env-section {
            {% comment %} margin: 24px 0; {% endcomment %}
            margin-top: 40px;
            padding-top: 0px;
        }

        .env-title {
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 16px;
            color: #2d3436;
        }

        .env-items {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .env-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 12px;
            background: #f8f9fa;
            border-radius: 10px;
        }

        .env-icon {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
        }

        .water-icon {
            background: #74b9ff;
            color: white;
        }

        .co2-icon {
            background: #fdcb6e;
            color: white;
        }

        .env-text {
            flex: 1;
        }

        .env-main {
            font-weight: 600;
            color: #20A090;
            margin-bottom: 2px;
        }

        .env-sub {
            font-size: 12px;
            color: #636e72;
        }

        /* Related Items */
        .related-section {
            margin-top: 40px;
            padding-top: 0px;
            {% comment %} border-top: 1px solid #e9ecef; {% endcomment %}
        }

        .related-title {
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 20px;
            color: #2d3436;
        }

        .related-items {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .related-item {
            display: flex;
            gap: 16px;
            padding: 16px;
            background: #fff;
            border-radius: 12px;
            border: 1px solid #e9ecef;
            transition: all 0.2s;
        }

        .related-item:hover {
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            transform: translateY(-1px);
        }

        .related-image {
            width: 70px;
            height: 70px;
            border-radius: 10px;
            object-fit: cover;
            background: #f1f2f6;
        }

        .related-info {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .related-name {
            font-weight: 600;
            color: #2d3436;
            font-size: 14px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .related-desc {
            font-size: 12px;
            color: #636e72;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .related-price {
            font-weight: 700;
            color: #2d3436;
            margin-top: 4px;
        }

        .related-actions {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: flex-end;
        }

        .more-options {
            background: none;
            border: none;
            color: #636e72;
            cursor: pointer;
            padding: 4px;
        }

        .shop-btn {
            background: #20A090;
            color: white;
            border: none;
            padding: 6px 12px;
            border-radius: 16px;
            font-size: 12px;
            font-weight: 500;
            cursor: pointer;
            transition: background 0.2s;
            white-space: nowrap;
        }

        .shop-btn:hover {
            background: #00b894;
        }

        /* Bottom Navigation */
        .bottom-nav {
            position: fixed;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            max-width: 375px;
            width: 100%;
            background: white;
            border-top: 1px solid #e9ecef;
            padding: 10px 0;
        }

        .nav-indicator {
            width: 40px;
            height: 4px;
            background: #ddd;
            border-radius: 2px;
            margin: 0 auto;
        }

        /* Item menu bottom-sheet */
        .overlay {
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.4);
            display: none;
            z-index: 1000;
        }
        .item-menu {
            position: fixed;
            left: 50%;
            bottom: 0;
            transform: translate(-50%, 100%);
            width: 100%;
            max-width: 375px;
            background: #fff;
            border-radius: 16px 16px 0 0;
            box-shadow: 0 -8px 24px rgba(0,0,0,0.15);
            padding: 12px 0;
            transition: transform .25s ease;
        }
        .item-menu .handle {
            width: 40px;
            height: 4px;
            background: #e5e7eb;
            border-radius: 2px;
            margin: 8px auto 12px;
        }
        .item-menu .title {
            text-align: center;
            font-weight: 600;
            color: #2d3436;
            margin-bottom: 8px;
        }
        .item-menu .list {
            display: flex;
            flex-direction: column;
        }
        .item-menu .list button {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            background: transparent;
            border: none;
            padding: 14px 16px;
            font-size: 14px;
            color: #2d3436;
            cursor: pointer;
        }
        .item-menu .list button + button { border-top: 1px solid #f0f0f0; }
        .overlay.show { display: block; animation: fadeIn 0.2s ease-out; }
        .overlay.show .item-menu { transform: translate(-50%, 0); animation: slideUp 0.3s ease-out; }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
        @keyframes slideUp { from { transform: translate(-50%, 100%); } to { transform: translate(-50%, 0); } }

        /* Textile Exchange Modal */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0,0,0,0.7);
            backdrop-filter: blur(10px);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
        }
        
        .modal-overlay.active {
            opacity: 1;
            visibility: visible;
        }
        
        .modal-container {
            max-width: 400px;
            width: 90%;
            max-height: 90vh;
            background: white;
            border-radius: 24px;
            box-shadow: 0 25px 60px rgba(0,0,0,0.3);
            transform: scale(0.7) translateY(50px);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            overflow: hidden;
            position: relative;
        }
        
        .modal-overlay.active .modal-container {
            transform: scale(1) translateY(0);
        }
        
        .modal-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            position: relative;
            text-align: center;
        }
        
        .close-button {
            position: absolute;
            top: 15px;
            right: 15px;
            width: 35px;
            height: 35px;
            border-radius: 50%;
            background: rgba(255,255,255,0.2);
            border: none;
            color: white;
            font-size: 18px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
        }
        
        .close-button:hover {
            background: rgba(255,255,255,0.3);
            transform: scale(1.1);
        }
        
        .modal-title {
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 5px;
        }
        
        .modal-subtitle {
            font-size: 14px;
            opacity: 0.9;
        }
        
        .certification-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(52, 199, 89, 0.2);
            border: 1px solid rgba(52, 199, 89, 0.5);
            border-radius: 15px;
            padding: 6px 12px;
            margin-top: 10px;
            font-size: 12px;
            font-weight: 600;
        }
        
        .status-dot {
            width: 6px;
            height: 6px;
            background: #34C759;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(52, 199, 89, 0.7); }
            70% { box-shadow: 0 0 0 8px rgba(52, 199, 89, 0); }
            100% { box-shadow: 0 0 0 0 rgba(52, 199, 89, 0); }
        }
        
        .modal-content {
            max-height: 60vh;
            overflow-y: auto;
            scrollbar-width: thin;
            scrollbar-color: #667eea transparent;
        }
        
        .modal-content::-webkit-scrollbar {
            width: 6px;
        }
        
        .modal-content::-webkit-scrollbar-track {
            background: transparent;
        }
        
        .modal-content::-webkit-scrollbar-thumb {
            background: #667eea;
            border-radius: 3px;
        }
        
        .company-info {
            padding: 25px;
            border-bottom: 1px solid #f0f0f0;
        }
        
        .company-header {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 15px;
        }
        
        .company-logo {
            width: 50px;
            height: 50px;
            border-radius: 15px;
            background: linear-gradient(135deg, #FF6B35, #F7931E, #1E88E5);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            font-weight: bold;
            font-size: 12px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.15);
        }
        
        .company-details h3 {
            font-size: 18px;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 5px;
        }
        
        .company-dates {
            font-size: 12px;
            color: #666;
        }
        
        .validity-info {
            background: linear-gradient(135deg, #E8F5E8, #F1F8E9);
            border-radius: 12px;
            padding: 12px;
            border-left: 4px solid #34C759;
        }
        
        .validity-title {
            font-size: 11px;
            font-weight: 600;
            color: #2E7D32;
            margin-bottom: 3px;
        }
        
        .validity-date {
            font-size: 13px;
            font-weight: 700;
            color: #1B5E20;
        }
        
        .section {
            padding: 20px 25px;
        }
        
        .section:not(:last-child) {
            border-bottom: 1px solid #f0f0f0;
        }
        
        .section-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 15px;
        }
        
        .section-title {
            font-size: 16px;
            font-weight: 700;
            color: #1a1a1a;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .section-count {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 3px 8px;
            border-radius: 10px;
            font-size: 11px;
            font-weight: 600;
        }
        
        .facility-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #f8f9fa;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 10px;
            transition: all 0.2s ease;
            border-left: 3px solid transparent;
        }
        
        .facility-item:hover {
            background: #f0f1f5;
            border-left-color: #667eea;
            transform: translateX(5px);
        }
        
        .facility-left {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .facility-icon {
            width: 36px;
            height: 36px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            font-size: 16px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.15);
        }
        
        .facility-icon.retail {
            background: linear-gradient(135deg, #FF416C, #FF4B2B);
        }
        
        .facility-icon.retail::before {
            content: '💰';
        }
        
        .facility-icon.trading {
            background: linear-gradient(135deg, #667eea, #764ba2);
        }
        
        .facility-icon.trading::before {
            content: '📊';
        }
        
        .facility-icon.brand {
            background: linear-gradient(135deg, #f093fb, #f5576c);
        }
        
        .facility-icon.brand::before {
            content: '🎨';
        }
        
        .facility-info h4 {
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 2px;
            color: #1a1a1a;
        }
        
        .facility-info .code {
            font-size: 11px;
            color: #666;
        }
        
        .facility-badges {
            display: flex;
            gap: 5px;
        }
        
        .badge {
            padding: 4px 8px;
            border-radius: 8px;
            font-size: 9px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .badge.grs {
            background: #E8F5E8;
            color: #2E7D32;
            border: 1px solid #C8E6C9;
        }
        
        .badge.rcs {
            background: #E3F2FD;
            color: #1565C0;
            border: 1px solid #BBDEFB;
        }
        
        .material-item {
            display: flex;
            align-items: center;
            gap: 15px;
            background: #f8f9fa;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 10px;
            transition: all 0.2s ease;
        }
        
        .material-item:hover {
            background: #f0f1f5;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        }
        
        .material-progress {
            width: 42px;
            height: 42px;
            position: relative;
            border-radius: 50%;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            border: 3px solid #fff;
        }
        
        .progress-circle {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            font-weight: 700;
            color: #fff;
            text-shadow: 0 1px 2px rgba(0,0,0,0.3);
        }
        
        .progress-100 {
            background: linear-gradient(135deg, #4CAF50, #66BB6A);
        }
        
        .progress-70 {
            background: conic-gradient(from 0deg, #FF9800 0deg, #FFA726 252deg, #E0E0E0 252deg);
        }
        
        .progress-50 {
            background: conic-gradient(from 0deg, #BDBDBD 0deg, #E0E0E0 180deg, #F5F5F5 180deg);
            color: #666;
        }
        
        .material-info h4 {
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 2px;
            color: #1a1a1a;
        }
        
        .material-info .code {
            font-size: 11px;
            color: #666;
        }

        /* Patagonia Inc. Modal */
        .patagonia-modal {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0,0,0,0.7);
            backdrop-filter: blur(10px);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
        }
        
        .patagonia-modal.active {
            opacity: 1;
            visibility: visible;
        }
        
        .patagonia-container {
            width: 100%;
            max-width: 375px;
            max-height: 90vh;
            background: white;
            border-radius: 30px;
            overflow: hidden;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            position: relative;
            transform: scale(0.7) translateY(50px);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: flex;
            flex-direction: column;
        }
        
        .patagonia-modal.active .patagonia-container {
            transform: scale(1) translateY(0);
        }
        
        .patagonia-header {
            background: linear-gradient(135deg, #f4d03f 0%, #52c9a8 100%);
            padding: 30px 20px 20px;
            position: relative;
            color: white;
            flex-shrink: 0;
        }
        
        
        .patagonia-close-btn {
            position: absolute;
            top: 20px;
            right: 20px;
            width: 30px;
            height: 30px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
            border: none;
            color: white;
            font-size: 16px;
        }
        
        .patagonia-close-btn:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: scale(1.1);
        }
        
        .patagonia-company-name {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 10px;
            color: #2c3e50;
        }
        
        .patagonia-status-badge {
            background: rgba(255, 255, 255, 0.9);
            color: #52c9a8;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 600;
            display: inline-block;
        }
        
        .patagonia-content {
            padding: 30px 20px;
            flex: 1;
            overflow-y: auto;
            scrollbar-width: thin;
            scrollbar-color: #52c9a8 transparent;
        }
        
        .patagonia-content::-webkit-scrollbar {
            width: 6px;
        }
        
        .patagonia-content::-webkit-scrollbar-track {
            background: transparent;
        }
        
        .patagonia-content::-webkit-scrollbar-thumb {
            background: #52c9a8;
            border-radius: 3px;
        }
        
        .patagonia-date-info {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 15px;
            margin-bottom: 30px;
            border-left: 4px solid #52c9a8;
        }
        
        .patagonia-date-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
            font-size: 14px;
            color: #666;
        }
        
        .patagonia-date-row:last-child {
            margin-bottom: 0;
        }
        
        .patagonia-section-title {
            font-size: 20px;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 20px;
        }
        
        .patagonia-business-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 15px 0;
            border-bottom: 1px solid #eee;
        }
        
        .patagonia-business-item:last-child {
            border-bottom: none;
        }
        
        .patagonia-business-info {
            flex: 1;
        }
        
        .patagonia-business-code {
            font-size: 12px;
            color: #999;
            margin-bottom: 5px;
        }
        
        .patagonia-business-name {
            font-size: 16px;
            font-weight: 600;
            color: #2c3e50;
        }
        
        .patagonia-status-buttons {
            display: flex;
            gap: 8px;
        }
        
        .patagonia-status-btn {
            padding: 6px 12px;
            border-radius: 15px;
            font-size: 12px;
            font-weight: 500;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .patagonia-status-btn.grs {
            background: #e8f5f3;
            color: #52c9a8;
        }
        
        .patagonia-status-btn.rcs {
            background: #e3f2fd;
            color: #2196f3;
        }
        
        .patagonia-status-btn:hover {
            transform: translateY(-1px);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }
        
        .patagonia-progress-section {
            margin-top: 40px;
        }
        
        .patagonia-progress-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 15px;
        }
        
        .patagonia-progress-item {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .patagonia-progress-circle {
            width: 60px;
            height: 60px;
            margin: 0 auto 15px;
            position: relative;
        }
        
        .patagonia-circle-bg, .patagonia-circle-progress {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            position: absolute;
            top: 0;
            left: 0;
        }
        
        .patagonia-circle-bg {
            background: #f0f0f0;
        }
        
        .patagonia-circle-progress {
            background: conic-gradient(#52c9a8 0deg, #52c9a8 var(--progress), #f0f0f0 var(--progress));
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            color: #2c3e50;
            font-size: 14px;
        }
        
        .patagonia-progress-label {
            font-size: 12px;
            color: #52c9a8;
            margin-bottom: 5px;
            font-weight: 600;
        }
        
        .patagonia-progress-subtitle {
            font-size: 10px;
            color: #666;
            margin-top: 2px;
            font-weight: 400;
        }
        
        
        .patagonia-progress-item.yellow .patagonia-circle-progress {
            background: conic-gradient(#f39c12 0deg, #f39c12 var(--progress), #f0f0f0 var(--progress));
        }
        
        .patagonia-progress-item.yellow .patagonia-progress-label {
            color: #f39c12;
        }
        
        .patagonia-progress-item.full {
            grid-column: 1 / -1;
        }
        
        .patagonia-bottom-indicator {
            width: 60px;
            height: 4px;
            background: #ddd;
            border-radius: 2px;
            margin: 30px auto 20px;
        }


        @media (max-width: 375px) {
            .container {
                max-width: 100%;
            }
            
            .bottom-nav {
                max-width: 100%;
            }
        }

        @media (min-width: 376px) {
            .container {
                border: 1px solid #e9ecef;
                border-radius: 0;
                margin-top: 20px;
                margin-bottom: 20px;
            }
        }

        /* Animations */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .product-info, .env-section, .related-section {
            animation: fadeInUp 0.6s ease-out;
        }

        /* Floating heart button over image */
        .heart-btn {
            position: absolute;
            right: 16px;
            bottom: -12px;
            width: 44px;
            height: 44px;
            border-radius: 50%;
            border: 1px solid rgba(0,0,0,0.05);
            background: #ffffff;
            color: #ff4757;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 6px 18px rgba(0,0,0,0.18);
            cursor: pointer;
            transition: box-shadow .2s ease, color .15s ease;
        }
        .heart-btn svg { display: block; transition: transform .15s ease; }
        .heart-btn .heart-fill { display: none; }
        .heart-btn .heart-outline { display: block; }
        .heart-btn.filled .heart-fill { display: block; }
        .heart-btn.filled .heart-outline { display: none; }
        .heart-btn:hover { background: #ffffff; box-shadow: 0 8px 22px rgba(0,0,0,0.22); color: #ff2d55; }
        .heart-btn:hover svg { transform: scale(1.08); }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header with product image -->
        <div class="header">
            <img src="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=375&h=400&fit=crop&crop=center" alt="미니멀 테일러드" class="product-image">
            <div class="nav-buttons">
                <button class="back-btn">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                        <path d="M15 18l-6-6 6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </button>
            </div>
            <button class="heart-btn" aria-pressed="false">
                <svg class="heart-fill" width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
                </svg>
                <svg class="heart-outline" width="20" height="20" viewBox="0 0 24 24" fill="none">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
            </button>
        </div>

        <!-- Product Information -->
        <div class="product-info">
            <h1 class="product-title">미니멀 테일러드</h1>
            <p class="product-description">
                오가닉 코튼 simple and elegant shape makes it perfect for those of you who like you who want minimalist clothes 
                <a href="#" class="read-more">Read More...</a>
            </p>

            <!-- Audio Player -->
            <div class="audio-player">
                <button class="play-btn" onclick="togglePlay()">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" id="playIcon">
                        <polygon points="5,3 19,12 5,21"/>
                    </svg>
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" id="pauseIcon" style="display: none;">
                        <rect x="6" y="4" width="4" height="16"/>
                        <rect x="14" y="4" width="4" height="16"/>
                    </svg>
                </button>
                <div class="audio-info">
                    <div class="audio-time">0:00 / 1:23</div>
                    <div class="progress-bar">
                        <div class="progress" id="progress"></div>
                    </div>
                </div>
                <button class="volume-btn">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                        <polygon points="11,5 6,9 2,9 2,15 6,15 11,19"/>
                        <path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/>
                    </svg>
                </button>
                <button class="more-btn">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                        <circle cx="12" cy="12" r="1"/>
                        <circle cx="12" cy="5" r="1"/>
                        <circle cx="12" cy="19" r="1"/>
                    </svg>
                </button>
            </div>

            <!-- Environmental Impact -->
            <div class="env-section">
                <h2 class="env-title">환경 효과</h2>
                <div class="env-items">
                    <div class="env-item">
                        <div class="env-icon water-icon">💧</div>
                        <div class="env-text">
                            <div class="env-main">물 250ml 절약</div>
                            <div class="env-sub">WATER</div>
                        </div>
                    </div>
                    <div class="env-item">
                        <div class="env-icon co2-icon">🌱</div>
                        <div class="env-text">
                            <div class="env-main">탄소배출 35-40% 감소</div>
                            <div class="env-sub">CO2</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Related Items -->
            <div class="related-section">
                <h2 class="related-title">리사이클 아이템</h2>
                <div class="related-items">
                    <div class="related-item">
                        <div class="related-image" style="background: url('https://images.unsplash.com/photo-1586790170083-2f9ceadc732d?w=70&h=70&fit=crop') center/cover;"></div>
                        <div class="related-info">
                            <div class="related-name">Modern light clothes</div>
                            <div class="related-desc">폐의류 재활용 섬유 사용</div>
                            <div class="related-price">$212.99</div>
                        </div>
                        <div class="related-actions">
                            <button class="more-options">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                                    <circle cx="12" cy="12" r="1"/>
                                    <circle cx="19" cy="12" r="1"/>
                                    <circle cx="5" cy="12" r="1"/>
                                </svg>
                            </button>
                            <button class="shop-btn">웹사이트</button>
                        </div>
                    </div>
                    
                    <div class="related-item">
                        <div class="related-image" style="background: url('https://images.unsplash.com/photo-1473966968600-fa801b869a1a?w=70&h=70&fit=crop') center/cover;"></div>
                        <div class="related-info">
                            <div class="related-name">Modern black pants</div>
                            <div class="related-desc">폐플라스틱병 재활용 원단</div>
                            <div class="related-price">$162.99</div>
                        </div>
                        <div class="related-actions">
                            <button class="more-options">
                                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                                    <circle cx="12" cy="12" r="1"/>
                                    <circle cx="19" cy="12" r="1"/>
                                    <circle cx="5" cy="12" r="1"/>
                                </svg>
                            </button>
                            <button class="shop-btn">웹사이트</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Bottom Navigation -->
        <div class="bottom-nav">
            <div class="nav-indicator"></div>
        </div>
    </div>

    <!-- Item menu bottom sheet overlay -->
    <div class="overlay" id="itemMenuOverlay" role="dialog" aria-modal="true" aria-labelledby="itemMenuTitle">
        <div class="item-menu">
            <div class="handle"></div>
            <div class="title" id="itemMenuTitle">Modern black pants</div>
            <div class="list">
                <button type="button">리사이클 인증서 보기
                    <span>✅</span>
                </button>
                <button type="button">브랜드 ESG 보고서 보기
                    <span>📄</span>
                </button>
                <button type="button">추천 근거 보기
                    <span>❓</span>
                </button>
            </div>
        </div>
    </div>

    <!-- Textile Exchange Modal -->
    <div class="modal-overlay" id="textileModal" onclick="closeTextileModal(event)">
        <div class="modal-container" onclick="event.stopPropagation()">
            <!-- 모달 헤더 -->
            <div class="modal-header">
                <button class="close-button" onclick="closeTextileModal()">×</button>
                <h2 class="modal-title">Textile Exchange</h2>
                <p class="modal-subtitle">지속가능한 섬유 인증서</p>
                <div class="certification-badge">
                    <div class="status-dot"></div>
                    인증 유효
                </div>
            </div>
            
            <!-- 모달 콘텐츠 -->
            <div class="modal-content">
                <!-- 회사 정보 -->
                <div class="company-info">
                    <div class="company-header">
                        <div class="company-logo">patagonia</div>
                        <div class="company-details">
                            <h3>Patagonia Inc.</h3>
                            <div class="company-dates">
                                발급일: 2024-11-22
                            </div>
                        </div>
                    </div>
                    <div class="validity-info">
                        <div class="validity-title">유효 기간</div>
                        <div class="validity-date">2025년 11월 22일까지</div>
                    </div>
                </div>
                
                <!-- 시설 섹션 -->
                <div class="section">
                    <div class="section-header">
                        <h3 class="section-title">
                            🏭 시설 현황
                        </h3>
                        <div class="section-count">3개</div>
                    </div>
                    
                    <div class="facility-item">
                        <div class="facility-left">
                            <div class="facility-icon retail"></div>
                            <div class="facility-info">
                                <h4>Retail Sales</h4>
                                <div class="code">PRO025 • 소매/판매</div>
                            </div>
                        </div>
                        <div class="facility-badges">
                            <span class="badge grs">GRS</span>
                            <span class="badge rcs">RCS</span>
                        </div>
                    </div>
                    
                    <div class="facility-item">
                        <div class="facility-left">
                            <div class="facility-icon trading"></div>
                            <div class="facility-info">
                                <h4>Trading</h4>
                                <div class="code">PRO030 • 거래/유통</div>
                            </div>
                        </div>
                        <div class="facility-badges">
                            <span class="badge grs">GRS</span>
                            <span class="badge rcs">RCS</span>
                        </div>
                    </div>
                    
                    <div class="facility-item">
                        <div class="facility-left">
                            <div class="facility-icon brand"></div>
                            <div class="facility-info">
                                <h4>Brand Activity</h4>
                                <div class="code">PRO035 • 브랜드 활동</div>
                            </div>
                        </div>
                        <div class="facility-badges">
                            <span class="badge grs">GRS</span>
                            <span class="badge rcs">RCS</span>
                        </div>
                    </div>
                </div>
                
                <!-- 소재 섹션 -->
                <div class="section">
                    <div class="section-header">
                        <h3 class="section-title">
                            🧵 재활용 소재
                        </h3>
                        <div class="section-count">3개</div>
                    </div>
                    
                    <div class="material-item">
                        <div class="material-progress">
                            <div class="progress-circle progress-100">100%</div>
                        </div>
                        <div class="material-info">
                            <h4>Recycled Nylon</h4>
                            <div class="code">RM085 • 재활용 나일론</div>
                        </div>
                    </div>
                    
                    <div class="material-item">
                        <div class="material-progress">
                            <div class="progress-circle progress-70">70%</div>
                        </div>
                        <div class="material-info">
                            <h4>Recycled Polyester</h4>
                            <div class="code">RM089 • 재활용 폴리에스터</div>
                        </div>
                    </div>
                    
                    <div class="material-item">
                        <div class="material-progress">
                            <div class="progress-circle progress-50">50%</div>
                        </div>
                        <div class="material-info">
                            <h4>Recycled Cotton</h4>
                            <div class="code">RM023 • 재활용 면</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Patagonia Inc. Modal -->
    <div class="patagonia-modal" id="patagoniaModal" onclick="closePatagoniaModal(event)">
        <div class="patagonia-container" onclick="event.stopPropagation()">
            <div class="patagonia-header">
                <div class="patagonia-close-btn" onclick="closePatagoniaModal()">✕</div>
                
                <div class="patagonia-company-name">Patagonia Inc.</div>
                <div class="patagonia-status-badge">인증 유효</div>
            </div>

            <div class="patagonia-content">
                <div class="patagonia-date-info">
                    <div class="patagonia-date-row">
                        <span>발급일:</span>
                        <span>2024-11-22</span>
                    </div>
                    <div class="patagonia-date-row">
                        <span>만료일:</span>
                        <span>2025-11-22</span>
                    </div>
                </div>

                <div class="patagonia-section-title">사업 현황</div>
                
                <div class="patagonia-business-list">
                    <div class="patagonia-business-item">
                        <div class="patagonia-business-info">
                            <div class="patagonia-business-code">PRO025 • 소매/판매</div>
                            <div class="patagonia-business-name">Retail Sales</div>
                        </div>
                        <div class="patagonia-status-buttons">
                            <button class="patagonia-status-btn grs">GRS</button>
                            <button class="patagonia-status-btn rcs">RCS</button>
                        </div>
                    </div>

                    <div class="patagonia-business-item">
                        <div class="patagonia-business-info">
                            <div class="patagonia-business-code">PRO030 • 거래/유통</div>
                            <div class="patagonia-business-name">Trading</div>
                        </div>
                        <div class="patagonia-status-buttons">
                            <button class="patagonia-status-btn grs">GRS</button>
                            <button class="patagonia-status-btn rcs">RCS</button>
                        </div>
                    </div>

                    <div class="patagonia-business-item">
                        <div class="patagonia-business-info">
                            <div class="patagonia-business-code">PRO035 • 브랜드 활동</div>
                            <div class="patagonia-business-name">Brand</div>
                        </div>
                        <div class="patagonia-status-buttons">
                            <button class="patagonia-status-btn grs">GRS</button>
                            <button class="patagonia-status-btn rcs">RCS</button>
                        </div>
                    </div>
                </div>

                <div class="patagonia-progress-section">
                    <div class="patagonia-section-title">재활용 소재</div>
                    
                    <div class="patagonia-progress-grid">
                        <div class="patagonia-progress-item">
                            <div class="patagonia-progress-circle">
                                <div class="patagonia-circle-bg"></div>
                                <div class="patagonia-circle-progress" style="--progress: 360deg;">100%</div>
                            </div>
                            <div class="patagonia-progress-label">재활용 나일론</div>
                            <div class="patagonia-progress-subtitle">Overcoats, jackets, vests</div>
                        </div>

                        <div class="patagonia-progress-item">
                            <div class="patagonia-progress-circle">
                                <div class="patagonia-circle-bg"></div>
                                <div class="patagonia-circle-progress" style="--progress: 360deg;">100%</div>
                            </div>
                            <div class="patagonia-progress-label">재활용 폴리에스터</div>
                            <div class="patagonia-progress-subtitle">Overcoats, jackets, vests</div>
                        </div>

                        <div class="patagonia-progress-item yellow">
                            <div class="patagonia-progress-circle">
                                <div class="patagonia-circle-bg"></div>
                                <div class="patagonia-circle-progress" style="--progress: 198deg;">55%</div>
                            </div>
                            <div class="patagonia-progress-label">재활용 폴리에스터</div>
                            <div class="patagonia-progress-subtitle">Overcoats, jackets, vests</div>
                        </div>

                        <div class="patagonia-progress-item yellow">
                            <div class="patagonia-progress-circle">
                                <div class="patagonia-circle-bg"></div>
                                <div class="patagonia-circle-progress" style="--progress: 180deg;">50%</div>
                            </div>
                            <div class="patagonia-progress-label">재활용 폴리에스터</div>
                            <div class="patagonia-progress-subtitle">Overcoats, jackets, vests</div>
                        </div>
                    </div>

                    <div class="patagonia-progress-item yellow full">
                        <div class="patagonia-progress-circle">
                            <div class="patagonia-circle-bg"></div>
                            <div class="patagonia-circle-progress" style="--progress: 180deg;">50%</div>
                        </div>
                        <div class="patagonia-progress-label">재활용 면</div>
                        <div class="patagonia-progress-subtitle">Overcoats, jackets, vests</div>
                        <div class="patagonia-progress-subtitle">Activewear, sportswear</div>
                    </div>
                </div>

                <div class="patagonia-bottom-indicator"></div>
            </div>
        </div>
    </div>

    <script>
        let isPlaying = false;
        let progress = 0;
        let progressInterval;

        function togglePlay() {
            const playIcon = document.getElementById('playIcon');
            const pauseIcon = document.getElementById('pauseIcon');
            const progressBar = document.getElementById('progress');

            isPlaying = !isPlaying;

            if (isPlaying) {
                playIcon.style.display = 'none';
                pauseIcon.style.display = 'block';
                startProgress();
            } else {
                playIcon.style.display = 'block';
                pauseIcon.style.display = 'none';
                stopProgress();
            }
        }

        function startProgress() {
            progressInterval = setInterval(() => {
                progress += 1;
                if (progress >= 100) {
                    progress = 100;
                    togglePlay();
                }
                document.getElementById('progress').style.width = progress + '%';
                
                // Update time display
                const currentTime = Math.floor((progress / 100) * 83); // 1:23 = 83 seconds
                const minutes = Math.floor(currentTime / 60);
                const seconds = currentTime % 60;
                document.querySelector('.audio-time').textContent = 
                    `${minutes}:${seconds.toString().padStart(2, '0')} / 1:23`;
            }, 100);
        }

        function stopProgress() {
            if (progressInterval) {
                clearInterval(progressInterval);
            }
        }

        // Smooth scroll behavior for read more link
        document.querySelector('.read-more').addEventListener('click', (e) => {
            e.preventDefault();
            // Here you would typically expand the description or navigate to full details
            alert('더 자세한 정보를 보여줍니다.');
        });

        // Add click handlers for shop buttons
        document.querySelectorAll('.shop-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                alert('공식 사이트로 이동합니다.');
            });
        });

        // Bottom-sheet menu open/close
        const overlay = document.getElementById('itemMenuOverlay');
        function openItemMenu(titleText) {
            const titleEl = document.getElementById('itemMenuTitle');
            if (titleEl && titleText) titleEl.textContent = titleText;
            // Reset to browser bottom
            const sheet = overlay.querySelector('.item-menu');
            if (sheet) sheet.style.bottom = '0px';
            overlay.classList.add('show');
        }
        function closeItemMenu() {
            overlay.classList.remove('show');
        }
        overlay.addEventListener('click', (e) => {
            // close when clicking backdrop area outside sheet
            if (e.target === overlay) closeItemMenu();
        });
        document.querySelectorAll('.more-options').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const item = e.currentTarget.closest('.related-item');
                const name = item?.querySelector('.related-name')?.textContent?.trim();
                openItemMenu(name || '항목 메뉴');
            });
        });

        // Item menu button handlers
        const menuButtons = document.querySelectorAll('.item-menu .list button');
        if (menuButtons.length >= 3) {
            // First button: Patagonia Inc. Modal
            menuButtons[0].addEventListener('click', () => {
                closeItemMenu();
                openPatagoniaModal();
            });

            // Second button: Brand website
            menuButtons[1].addEventListener('click', () => {
                closeItemMenu();
                // Navigate to brand website
                window.location.href = '/brand-website';
            });

            // Third button: Recommendation basis with vector DB highlights
            menuButtons[2].addEventListener('click', () => {
                closeItemMenu();
                // Navigate to recommendation basis page
                window.location.href = '/recommendation-basis';
            });
        }

        // Back button handler
        document.querySelector('.back-btn').addEventListener('click', () => {
            if (window.history.length > 1) {
                window.history.back();
            } else {
                alert('이전 페이지로 돌아갑니다.');
            }
        });


        // Heart button toggle
        const heartBtn = document.querySelector('.heart-btn');
        // initial state: outlined (border-only)
        heartBtn.classList.remove('filled');
        heartBtn.setAttribute('aria-pressed', 'false');
        heartBtn.addEventListener('click', function() {
            const isFilled = this.classList.toggle('filled');
            this.setAttribute('aria-pressed', isFilled.toString());
        });

        // Textile Exchange Modal functions
        function openTextileModal() {
            const modal = document.getElementById('textileModal');
            modal.classList.add('active');
            document.body.style.overflow = 'hidden'; // 백그라운드 스크롤 방지
        }
        
        function closeTextileModal(event) {
            // 모달 컨테이너 내부 클릭 시에는 닫지 않음
            if (event && event.target !== event.currentTarget) return;
            
            const modal = document.getElementById('textileModal');
            modal.classList.remove('active');
            document.body.style.overflow = 'auto'; // 백그라운드 스크롤 복원
        }
        
        // ESC 키로 모달 닫기
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                closeTextileModal();
                closePatagoniaModal();
            }
        });

        // Patagonia Inc. Modal functions
        function openPatagoniaModal() {
            const modal = document.getElementById('patagoniaModal');
            modal.classList.add('active');
            document.body.style.overflow = 'hidden'; // 백그라운드 스크롤 방지
        }
        
        function closePatagoniaModal(event) {
            // 모달 컨테이너 내부 클릭 시에는 닫지 않음
            if (event && event.target !== event.currentTarget) return;
            
            const modal = document.getElementById('patagoniaModal');
            modal.classList.remove('active');
            document.body.style.overflow = 'auto'; // 백그라운드 스크롤 복원
        }

        // Patagonia modal interactions
        document.querySelectorAll('.patagonia-status-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                this.style.transform = 'scale(0.95)';
                setTimeout(() => {
                    this.style.transform = 'scale(1)';
                }, 150);
            });
        });
    </script>
</body>
</html>