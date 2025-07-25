'use client';

import { useState } from 'react';

export default function BasicVariables() {
  const [output, setOutput] = useState('');

  // 예제 실행 함수
  const runExample = () => {
    let result = '';

    // 1. let 변수 (재할당 가능)
    let userName = '김철수';
    result += `1. let 변수:\n`;
    result += `   userName = '${userName}'\n`;
    
    userName = '이영희'; // 재할당 가능
    result += `   userName = '${userName}' (재할당 후)\n\n`;

    // 2. const 상수 (재할당 불가)
    const siteName = '티켓 예약 시스템';
    result += `2. const 상수:\n`;
    result += `   siteName = '${siteName}'\n`;
    result += `   (const는 재할당 불가능)\n\n`;

    // 3. var의 문제점 (사용하지 않는 이유)
    result += `3. var vs let 차이점:\n`;
    
    // 블록 스코프 예제
    {
      let blockLet = 'let은 블록 스코프';
      var blockVar = 'var는 함수 스코프';
    }
    
    result += `   let: 블록({}) 내에서만 접근 가능\n`;
    result += `   var: 함수 전체에서 접근 가능 (문제 발생 가능)\n\n`;

    // 4. 실제 티켓 시스템 예제
    result += `4. 티켓 시스템 예제:\n`;
    const maxTickets = 100;        // 최대 티켓 수 (변경 불가)
    let soldTickets = 45;          // 판매된 티켓 수 (변경 가능)
    let availableTickets = maxTickets - soldTickets;
    
    result += `   최대 티켓: ${maxTickets}장\n`;
    result += `   판매 완료: ${soldTickets}장\n`;
    result += `   남은 티켓: ${availableTickets}장\n`;

    setOutput(result);
  };

  return (
    <div className="example-container">
      <div className="example-info">
        <h3>🎯 학습 목표</h3>
        <ul>
          <li><code>let</code>과 <code>const</code>의 차이점 이해</li>
          <li><code>var</code>를 사용하지 않는 이유 알기</li>
          <li>블록 스코프 개념 이해</li>
          <li>실제 프로젝트에서의 변수 사용법</li>
        </ul>
      </div>

      <div className="code-section">
        <h3>📝 코드 예제</h3>
        <pre className="code-block">{`// 1. let: 재할당 가능한 변수
let userName = '김철수';
userName = '이영희';  // ✅ 가능

// 2. const: 재할당 불가능한 상수
const siteName = '티켓 예약 시스템';
// siteName = '다른 이름';  // ❌ 오류 발생

// 3. 티켓 시스템 실제 사용 예제
const maxTickets = 100;           // 최대 티켓 수
let soldTickets = 45;             // 현재 판매량
let availableTickets = maxTickets - soldTickets;

console.log(\`남은 티켓: \${availableTickets}장\`);`}</pre>
      </div>

      <div className="interactive-section">
        <button onClick={runExample} className="run-button">
          🚀 예제 실행하기
        </button>
        
        {output && (
          <div className="output-section">
            <h4>📤 실행 결과:</h4>
            <pre className="output">{output}</pre>
          </div>
        )}
      </div>

      <div className="tips-section">
        <h3>💡 실무 팁</h3>
        <div className="tip">
          <strong>언제 let을 사용할까?</strong>
          <p>값이 변경될 가능성이 있는 경우 (카운터, 사용자 입력, 계산 결과 등)</p>
        </div>
        <div className="tip">
          <strong>언제 const를 사용할까?</strong>
          <p>값이 변경되지 않는 경우 (설정값, API URL, 고정 메시지 등)</p>
        </div>
        <div className="tip">
          <strong>var는 왜 안 쓸까?</strong>
          <p>예상치 못한 스코프 문제로 버그가 발생할 수 있어서</p>
        </div>
      </div>

      <style>{`
        .example-container {
          border: 1px solid #e1e5e9;
          border-radius: 8px;
          padding: 20px;
          margin: 20px 0;
        }

        .example-info ul {
          background: #f8f9fa;
          padding: 15px;
          border-radius: 6px;
          margin: 10px 0;
        }

        .example-info li {
          margin: 8px 0;
        }

        .code-section {
          margin: 20px 0;
        }

        .code-block {
          background: #2d3748;
          color: #e2e8f0;
          padding: 20px;
          border-radius: 6px;
          overflow-x: auto;
          font-family: 'Fira Code', monospace;
          line-height: 1.5;
        }

        .interactive-section {
          margin: 20px 0;
          text-align: center;
        }

        .run-button {
          background: #48bb78;
          color: white;
          border: none;
          padding: 12px 24px;
          border-radius: 6px;
          font-size: 16px;
          cursor: pointer;
          transition: background 0.2s;
        }

        .run-button:hover {
          background: #38a169;
        }

        .output-section {
          margin-top: 20px;
          text-align: left;
        }

        .output {
          background: #1a202c;
          color: #68d391;
          padding: 15px;
          border-radius: 6px;
          border-left: 4px solid #48bb78;
          font-family: monospace;
          white-space: pre-wrap;
        }

        .tips-section {
          margin-top: 30px;
          background: #fffaf0;
          padding: 20px;
          border-radius: 6px;
          border-left: 4px solid #ed8936;
        }

        .tip {
          margin: 15px 0;
          padding: 10px;
          background: white;
          border-radius: 4px;
        }

        .tip strong {
          color: #c05621;
        }

        code {
          background: #edf2f7;
          padding: 2px 6px;
          border-radius: 3px;
          font-family: monospace;
          color: #2d3748;
        }
      `}</style>
    </div>
  );
}
