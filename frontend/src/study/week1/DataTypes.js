'use client';

import { useState } from 'react';

export default function DataTypes() {
  const [output, setOutput] = useState('');

  const runExample = () => {
    let result = '';

    // 1. 문자열 (String)
    result += `1. 문자열 (String):\n`;
    const eventName = '2024 K-POP 콘서트';
    const venue = "올림픽공원 체조경기장";
    const description = `${eventName}이 ${venue}에서 열립니다!`;
    
    result += `   eventName = "${eventName}"\n`;
    result += `   venue = "${venue}"\n`;
    result += `   템플릿 리터럴: "${description}"\n\n`;

    // 2. 숫자 (Number)
    result += `2. 숫자 (Number):\n`;
    const ticketPrice = 150000;      // 정수
    const discountRate = 0.15;       // 소수
    const finalPrice = ticketPrice * (1 - discountRate);
    
    result += `   ticketPrice = ${ticketPrice} (정수)\n`;
    result += `   discountRate = ${discountRate} (소수)\n`;
    result += `   finalPrice = ${finalPrice} (계산 결과)\n\n`;

    // 3. 불린 (Boolean)
    result += `3. 불린 (Boolean):\n`;
    const isVipTicket = true;
    const isSoldOut = false;
    const canPurchase = !isSoldOut && ticketPrice > 0;
    
    result += `   isVipTicket = ${isVipTicket}\n`;
    result += `   isSoldOut = ${isSoldOut}\n`;
    result += `   canPurchase = ${canPurchase} (논리 연산 결과)\n\n`;

    // 4. 배열 (Array)
    result += `4. 배열 (Array):\n`;
    const seatNumbers = ['A1', 'A2', 'B1', 'B2'];
    const prices = [150000, 150000, 120000, 120000];
    
    result += `   seatNumbers = [${seatNumbers.join(', ')}]\n`;
    result += `   prices = [${prices.join(', ')}]\n`;
    result += `   첫 번째 좌석: ${seatNumbers[0]}\n`;
    result += `   배열 길이: ${seatNumbers.length}\n\n`;

    // 5. 객체 (Object)
    result += `5. 객체 (Object):\n`;
    const ticket = {
      id: 'T001',
      eventName: '2024 K-POP 콘서트',
      seatNumber: 'A1',
      price: 150000,
      isVip: true,
      purchaseDate: '2024-07-25'
    };
    
    result += `   ticket = {\n`;
    result += `     id: "${ticket.id}",\n`;
    result += `     eventName: "${ticket.eventName}",\n`;
    result += `     seatNumber: "${ticket.seatNumber}",\n`;
    result += `     price: ${ticket.price},\n`;
    result += `     isVip: ${ticket.isVip}\n`;
    result += `   }\n`;
    result += `   티켓 ID: ${ticket.id}\n`;
    result += `   좌석 번호: ${ticket.seatNumber}\n\n`;

    // 6. null과 undefined
    result += `6. null과 undefined:\n`;
    let customerEmail = null;        // 의도적으로 비어있음
    let customerPhone;               // 아직 할당되지 않음 (undefined)
    
    result += `   customerEmail = ${customerEmail} (의도적으로 비워둠)\n`;
    result += `   customerPhone = ${customerPhone} (값이 할당되지 않음)\n\n`;

    // 7. typeof 연산자로 타입 확인
    result += `7. typeof 연산자로 타입 확인:\n`;
    result += `   typeof eventName = "${typeof eventName}"\n`;
    result += `   typeof ticketPrice = "${typeof ticketPrice}"\n`;
    result += `   typeof isVipTicket = "${typeof isVipTicket}"\n`;
    result += `   typeof seatNumbers = "${typeof seatNumbers}"\n`;
    result += `   typeof ticket = "${typeof ticket}"\n`;
    result += `   typeof customerEmail = "${typeof customerEmail}"\n`;
    result += `   typeof customerPhone = "${typeof customerPhone}"\n`;

    setOutput(result);
  };

  return (
    <div className="example-container">
      <div className="example-info">
        <h3>🎯 학습 목표</h3>
        <ul>
          <li><strong>문자열</strong>: 텍스트 데이터 다루기</li>
          <li><strong>숫자</strong>: 가격, 수량 등 계산하기</li>
          <li><strong>불린</strong>: 조건문에서 참/거짓 판단</li>
          <li><strong>배열</strong>: 여러 데이터를 순서대로 저장</li>
          <li><strong>객체</strong>: 관련 데이터를 그룹화</li>
          <li><strong>null/undefined</strong>: 빈 값의 차이점</li>
        </ul>
      </div>

      <div className="code-section">
        <h3>📝 코드 예제</h3>
        <pre className="code-block">{`// 1. 문자열 - 3가지 방법
const eventName = '2024 K-POP 콘서트';          // 작은따옴표
const venue = "올림픽공원 체조경기장";              // 큰따옴표
const info = \`\${eventName}이 \${venue}에서!\`;    // 템플릿 리터럴

// 2. 숫자 - 정수와 소수
const price = 150000;        // 정수
const discount = 0.15;       // 소수 (15%)
const final = price * (1 - discount);  // 계산

// 3. 불린 - 참/거짓
const isVip = true;
const soldOut = false;
const canBuy = !soldOut;     // 논리 연산

// 4. 배열 - 순서가 있는 데이터
const seats = ['A1', 'A2', 'B1'];
console.log(seats[0]);       // 'A1' (첫 번째)
console.log(seats.length);   // 3 (길이)

// 5. 객체 - 관련 데이터 그룹화
const ticket = {
  id: 'T001',
  seat: 'A1',
  price: 150000,
  vip: true
};
console.log(ticket.seat);    // 'A1'

// 6. 타입 확인
console.log(typeof price);   // "number"
console.log(typeof isVip);   // "boolean"`}</pre>
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

      <div className="comparison-table">
        <h3>📊 데이터 타입 비교표</h3>
        <table>
          <thead>
            <tr>
              <th>타입</th>
              <th>예시</th>
              <th>용도</th>
              <th>티켓 시스템 활용</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>String</td>
              <td>'안녕하세요'</td>
              <td>텍스트, 메시지</td>
              <td>이벤트명, 좌석번호, 사용자명</td>
            </tr>
            <tr>
              <td>Number</td>
              <td>150000</td>
              <td>가격, 수량, 계산</td>
              <td>티켓 가격, 재고 수량, 할인율</td>
            </tr>
            <tr>
              <td>Boolean</td>
              <td>true / false</td>
              <td>조건 판단</td>
              <td>VIP 여부, 매진 여부, 결제 완료</td>
            </tr>
            <tr>
              <td>Array</td>
              <td>['A1', 'A2']</td>
              <td>리스트, 목록</td>
              <td>좌석 목록, 가격표, 구매 내역</td>
            </tr>
            <tr>
              <td>Object</td>
              <td>{`{name: '콘서트'}`}</td>
              <td>데이터 그룹화</td>
              <td>티켓 정보, 사용자 정보, 이벤트 상세</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div className="tips-section">
        <h3>💡 실무 팁</h3>
        <div className="tip">
          <strong>문자열 결합은 템플릿 리터럴을 사용하세요!</strong>
          <p>❌ <code>"안녕 " + name + "님"</code><br/>
             ✅ <code>`안녕 &#36;&#123;name&#125;님`</code></p>
        </div>
        <div className="tip">
          <strong>숫자 계산 시 소수점 주의하세요!</strong>
          <p><code>0.1 + 0.2 = 0.30000000000000004</code> (부동소수점 오차)</p>
        </div>
        <div className="tip">
          <strong>배열과 객체는 참조 타입입니다!</strong>
          <p>복사할 때는 <code>[...array]</code> 또는 <code>&#123;...object&#125;</code> 사용</p>
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
          columns: 2;
          column-gap: 30px;
        }

        .example-info li {
          margin: 8px 0;
          break-inside: avoid;
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
          background: #38a169;
          color: white;
          border: none;
          padding: 12px 24px;
          border-radius: 6px;
          font-size: 16px;
          cursor: pointer;
          transition: background 0.2s;
        }

        .run-button:hover {
          background: #2f855a;
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
          border-left: 4px solid #38a169;
          font-family: monospace;
          white-space: pre-wrap;
          max-height: 400px;
          overflow-y: auto;
        }

        .comparison-table {
          margin: 30px 0;
        }

        table {
          width: 100%;
          border-collapse: collapse;
          margin: 15px 0;
        }

        th, td {
          border: 1px solid #e2e8f0;
          padding: 12px;
          text-align: left;
        }

        th {
          background: #f7fafc;
          font-weight: bold;
          color: #2d3748;
        }

        td {
          background: white;
        }

        tr:nth-child(even) td {
          background: #f8f9fa;
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

        @media (max-width: 768px) {
          .example-info ul {
            columns: 1;
          }
          
          table {
            font-size: 14px;
          }
          
          th, td {
            padding: 8px;
          }
        }
      `}</style>
    </div>
  );
}
