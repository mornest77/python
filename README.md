# API 規格文件

### 成績 api

可取得 `科目` `期中考成績`

#### Request

```http
GET /ntub/course
```

#### Response

|      Return       | Type | Description |
| :---------------: | :--: | :---------- |
|     course_id     |      | 科目代號    |
|    course_name    |      | 科目名稱    |
|  department_name  |      | 修課科別    |
| department_number |      | 科別代碼    |
|       grade       |      | 年級        |
|   class_number    |      | 班級        |
|    school_year    |      | 年度        |
|     semester      |      | 學期        |
|   midterm_score   |      | 期中考成績  |

```json
{
  "course_id": String,
  "course_name": 程式設計,
  "department_name": 資管,
  "department_number": 4,
  "grade": 1,
  "class_number": 4,
  "school_year": 2,
  "semester": 2,
  "midterm_score": 96
}
```
