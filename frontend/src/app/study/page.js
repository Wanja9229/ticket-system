'use client';

import Link from 'next/link';

export default function StudyMainPage() {
  return (
    <div className="container">
      <h1>프론트엔드 스터디 가이드 - 4주 완성</h1>
      <p>HTML/CSS 경험자가 React + Next.js 프로젝트 참여 가능한 수준 달성</p>
      
      <div className="study-overview">
        <h2>📋 전체 학습 로드맵</h2>
        <div className="week-grid">
          
          <div className="week-card">
            <h3>Week 1</h3>
            <h4>JavaScript 핵심 기초</h4>
            <p>변수, 함수, 배열, 객체 마스터</p>
            <Link href="/study/week1" className="study-link">
              학습 시작 →
            </Link>
          </div>

          <div className="week-card">
            <h3>Week 2</h3>
            <h4>React 컴포넌트와 상태</h4>
            <p>컴포넌트, Props, State, 이벤트 처리</p>
            <Link href="/study/week2" className="study-link">
              학습 시작 →
            </Link>
          </div>

          <div className="week-card">
            <h3>Week 3</h3>
            <h4>API 연동과 라우팅</h4>
            <p>데이터 페칭, useEffect, React Router</p>
            <Link href="/study/week3" className="study-link">
              학습 시작 →
            </Link>
          </div>

          <div className="week-card">
            <h3>Week 4</h3>
            <h4>Next.js와 실전 프로젝트</h4>
            <p>Next.js 기초, 실제 프로젝트 구조</p>
            <Link href="/study/week4" className="study-link">
              학습 시작 →
            </Link>
          </div>

        </div>
      </div>

      <div className="study-info">
        <h2>📚 학습 방법</h2>
        <ul>
          <li><strong>기간</strong>: 4주 (주 2회, 월/목)</li>
          <li><strong>1회 학습시간</strong>: 2-3시간</li>
          <li><strong>총 학습시간</strong>: 16-24시간</li>
          <li><strong>실습 중심</strong>: 티켓 시스템 관련 예제로 학습</li>
        </ul>
      </div>
    </div>
  );
}
